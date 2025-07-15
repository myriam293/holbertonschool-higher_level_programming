#!/usr/bin/python3
"""Unittests for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_first(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_max_middle(self):
        self.assertEqual(max_integer([12, 23, 40, 11, 2]), 40)

    def test_one_negative(self):
        self.assertEqual(max_integer([1, 2, -6, 7, 2]), 7)

    def test_all_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -5, -10]), -1)

    def test_single_element(self):
        self.assertEqual(max_integer([100]), 100)

    def test_identical_elements(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_floats_and_ints(self):
        self.assertEqual(max_integer([1.5, 2.6, 3.1, 2]), 3.1)

    def test_string_input(self):
        self.assertEqual(max_integer("Malvina"), 'v')  # Max char by ASCII

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["alpha", "zeta", "beta"]), "zeta")

    def test_none_input(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "Theo", 3])
