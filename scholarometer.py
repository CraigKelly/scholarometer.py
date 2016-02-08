"""scholarometer.py - single file Python module for accessing scholarometer.

Note that this module is designed and tested in Python3. No effort is currently
made to support Python 2
"""

# pylama:ignore=E128,E501

# TODO: rest of API

import logging
from urllib.parse import urlunparse, urljoin, quote

import requests  # External dep
from defusedxml.ElementTree import fromstring as xmlparse


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
        self.session = requests.Session()

    def _get_url(self, path, scheme=None, server=None, root=None):
        baseurl = urlunparse((
            scheme or self.scheme,
            server or self.server,
            root or self.root,
            None,
            None,
            None
        ))
        return urljoin(baseurl, path)

    def _log_response(self, resp):
        _log().info(
            "[%d]: Got %d bytes [First 8: '%s'] encoding:%s (app:%s)",
            resp.status_code,
            len(resp.content),
            resp.content[:8] if resp.content else '',
            resp.encoding,
            resp.apparent_encoding
        )

    def relative_get(self, path, api_root=None, params=None, headers=None):
        """Perform HTTP GET at endpoint path relative to the API root."""
        url = self._get_url(path, root=api_root)
        _log().info("Perfoming GET %s", url)

        resp = self.session.get(url, params=params, headers=headers)
        self._log_response(resp)

        if resp.status_code != 200:
            resp = None
        return resp

    def relative_post(self, path, api_root=None, params=None, data=None, headers=None):
        """Perform HTTP POST at endpoint path relative to the API root."""
        url = self._get_url(path, root=api_root)
        _log().info("Perfoming POST %s", url)

        resp = self.session.post(url, params=params, data=data, headers=headers)
        self._log_response(resp)

        if resp.status_code != 200:
            resp = None
        return resp


Config.DEFAULT_CONFIG = Config()


class Authors(object):
    """Provide the authors portion of the API."""

    def __init__(self, config=None):
        """Init the authors API with given config."""
        self.config = config or Config.DEFAULT_CONFIG

    def _author_parse(self, author):
        if not author:
            return None
        else:
            stats = author.find('statistics')
            return {
                'id': author.attrib['id'],
                'lastupdate': author.attrib['lastupdate'],
                'names': [n.text for n in author.find('names')],
                'article_count': int(stats.find('narticles').text),
                'citation_count': int(stats.find('ncitations').text),
            }

    def get_by_id(self, id):
        """Query author by scholarpedia ID: return a single author or None."""
        resp = self.config.relative_get('authors/id/' + quote(id))
        raw = resp.text if resp and resp.text else None
        if not raw:
            return None
        return self._author_parse(xmlparse(raw))

    def get_by_name(self, name):
        """Query author by name: returns a list of authors."""
        resp = self.config.relative_get('authors/name/' + quote(name))
        raw = resp.text if resp and resp.text else None
        if not raw:
            return []
        authors = xmlparse(raw)
        return [self._author_parse(author) for author in authors]

    def get_articles_by_id(self, id):
        """Return all articles published by the given author id."""
        resp = self.config.relative_post(
            'indexu.cgi',
            api_root='/cgi-bin/',
            headers={'Content-Type': 'text/plain;charset=UTF-8'},
            data='',
            params={
                'func': 'arrecords',
                'expr': id,
                'ver': '4.1.0'
            }
        )

        if len(resp.text) < 2:
            # Can't possibly be valid json
            return []

        return resp.json()
