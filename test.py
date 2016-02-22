#!/usr/bin/env python3
# pylama:ignore=D101,D102,E501

"""Unit testing for scholarometer module."""

import unittest  # yep, we're boring
import betamax   # Used for requests save/replay

from scholarometer import Authors


# Output logging to stderr (note that run_tests.sh sets our log level to DEBUG)
# if the env variable is set. This can be handy for things like betamax since
# we log some Requests info, and Requests itself will log a debug msg for actual
# HTTP stuff sent out into the world (which is missing when we're getting
# replays from betamax). You can use this like so:
# $ STDERR_LOGGING=1 ./run_tests.sh
import os
if os.environ.get('STDERR_LOGGING', None):
    import sys
    import logging
    stream_handler = logging.StreamHandler(sys.__stderr__)
    stream_handler.setFormatter(logging.Formatter('%(levelname)s :: %(name)s :: %(message)s'))
    logging.getLogger().addHandler(stream_handler)


# Test author API's
class AuthorTesting(unittest.TestCase):
    GRAESSER_ID = '1320f77a0cfb40fba374a9fef8d6d72d'
    CASSETTE_LIBRARY_DIR = ".cassettes"

    def setUp(self):
        self.authors = Authors()
        # Use betamax to cache responses from scholarometer
        self.recorder = betamax.Betamax(
            self.authors.config.session,
            cassette_library_dir=self.CASSETTE_LIBRARY_DIR
        )
        self.recorder.use_cassette('Authors', record='new_episodes')
        self.recorder.start()

    def tearDown(self):
        self.recorder.stop()

    def test_get_by_id(self):
        self.assertIsNone(self.authors.get_by_id("zzzzzzzzzzzzzzzzzzzzzzzzzz"))

        resp = self.authors.get_by_id(self.GRAESSER_ID)
        self.assertIsNotNone(resp)
        print(resp)

    def test_get_by_name(self):
        resp = self.authors.get_by_name("yyyyyyyyyy")
        self.assertEquals(0, len(resp))

        resp = self.authors.get_by_name("graesser")
        self.assertTrue(len(resp) > 0)

        print(resp)

    def test_get_articles_by_id(self):
        resp = self.authors.get_articles_by_id("zzzzzzzzzzzzzzzzzzzzzzzzzz")
        self.assertEquals(0, len(resp))

        resp = self.authors.get_articles_by_id(self.GRAESSER_ID)
        self.assertTrue(len(resp) > 0)

        print("First item only: " + repr(resp[0]))
