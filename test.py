#!/usr/bin/env python3
# pylama:ignore=D101,D102

"""Unit testing for scholarometer module."""

import unittest

from scholarometer import Authors


class AuthorTesting(unittest.TestCase):
    def setUp(self):
        self.authors = Authors()

    def test_get_by_id(self):
        self.assertIsNone(self.authors.get_by_id("zzzzzzzzzzzzzzzzzzzzzzzzzz"))

        # the ID is Art Graesser
        resp = self.authors.get_by_id("1320f77a0cfb40fba374a9fef8d6d72d")
        self.assertIsNotNone(resp)
        print(resp)

    def test_get_by_name(self):
        resp = self.authors.get_by_name("yyyyyyyyyy")
        self.assertEquals(0, len(resp))

        resp = self.authors.get_by_name("graesser")
        self.assertTrue(len(resp) > 0)

        print(resp)
