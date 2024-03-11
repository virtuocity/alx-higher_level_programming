#!/usr/bin/python3
""" unittest module to show some tests"""


import unittest


class TestSomeThings(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_is_upper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == "__main__":
    unittest.main()