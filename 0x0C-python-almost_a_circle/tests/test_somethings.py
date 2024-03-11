#!/usr/bin/python3
""" unittest module to show some tests"""


import unittest


class TestSomeThings(unittest.TestCase):
    """ class to show some unit tests"""
    def test_upper(self):
        """ test upper - test upper case
            Args:
                self: unittest object
        """
        self.assertEqual('foo'.upper(), 'FOO')

    def test_is_upper(self):
        """ test upper - test upper case
            Args:
                self: unittest object
        """
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == "__main__":
    unittest.main()
