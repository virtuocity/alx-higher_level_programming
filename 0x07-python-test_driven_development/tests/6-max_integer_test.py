#!/usr/bin/python3
""" Test max integer in a list"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_positives(self):
        """ test positive numbers"""
        test_list = [12, 3, 4, 99, 8]
        self.assertEqual(max_integer(test_list), 99)

    def test_first_positive(self):
        """ test positive numbers"""
        test_list = [12, 3, 4, 6, 8]
        self.assertEqual(max_integer(test_list), 12)

    def test_last_positive(self):
        """ test positive numbers"""
        test_list = [2, 3, 4, 6, 8]
        self.assertEqual(max_integer(test_list), 8)

    def test_first_negatives(self):
        """ test negative numbers"""
        test_list = [-2, 3, 4, 5, 6]
        self.assertEqual(max_integer(test_list), 6)

    def test_all_negatives(self):
        test_list = [-90, -80, -99, -67, -56]
        self.assertEqual(max_integer(test_list), -56)

    def test_empty_list(self):
        """ tests an empty list"""
        test_list = []
        self.assertEqual(max_integer(test_list), None)

    def test_one_element(self):
        test_list = [8]
        self.assertEqual(max_integer(test_list), 8)
