"""scholarometer.py - single file Python module for accessing scholarometer.

Note that this module is designed and tested in Python3. No effort is currently
made to support Python 2
"""

# pylama:ignore=E128

import logging
from urllib.parse import urlunparse, urljoin, quote

import requests  # External dep
from defusedxml.ElementTree import fromstring as xmlparse

# TODO: It would be nice to have an API mock for unit testing


def _log():
    return logging.getLogger('scholarometer')


class Config(object):
    """An instance of this class is an imuutable configuration for API call.

    Currently only our default instance makes sense, so you can just ignore
    this class.
    """

    DEF_SCHEME = 'http'
    DEF_SERVER = 'scholarometer.indiana.edu'
    DEF_ROOT = '/api/'

    def __init__(self, scheme=None, server=None, root=None):
        """Set up the immutable config."""
        self.scheme = scheme or Config.DEF_SCHEME
        self.server = server or Config.DEF_SERVER
        self.root = root or Config.DEF_ROOT
        self.baseurl = urlunparse(
            (self.scheme, self.server, self.root, None, None, None)
        )

    def relative_get(self, path):
        """Create an absolute URL based on path, relative to the API root."""
        url = urljoin(self.baseurl, path)
        _log().info("Perfoming GET %s", url)
        resp = requests.get(url)
        _log().info("[%d]: Got %d bytes in encoding %s (apparent %s)",
            resp.status_code,
            len(resp.content),
            resp.encoding,
            resp.apparent_encoding
        )
        if resp.status_code != 200:
            resp = None
        return resp

Config.DEFAULT_CONFIG = Config()


class Authors(object):
    """Provide the authors portion of the API."""

    def __init__(self, config=None):
        """Init the authors API with given config."""
        self.config = config or Config.DEFAULT_CONFIG

    def get_by_id(self, id):
        """Query author by scholarpedia ID."""
        resp = self.config.relative_get('authors/id/' + quote(id))
        raw = resp.text if resp and resp.text else None
        if not raw:
            return None
        author = xmlparse(raw)
        return {
            'id': author.attrib['id'],
            'lastupdate': author.attrib['lastupdate'],
            'names': [n.text for n in author.find('names')]
        }
