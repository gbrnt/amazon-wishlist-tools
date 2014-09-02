"""
Tests for amazon-wishlist-tools - Useful tools for your Amazon wishlist
"""

import unittest
import amazon_wishlist_tools as awt


class Prettifying(unittest.TestCase):
    """Test the formatting of the wishlist dict"""

    def test_formatting_correct(self):
        wishlist = [
            {"name": "Long Amazon name because sellers like to fit as many"
                "words into the name as possible", "price": 98.53,
                "quantity": 7, "priority": 5},
            {"name": "Slightly shorter Amazon name", "price": 56.42,
                "quantity": 1, "priority": 2}
        ]

        expected_result = "+------------------------------------------------"
        "-------------------------------------+-------+----------+----------"
        "+\n|                                         Name                  "
        "                      | Price | Quantity | Priority |\n+-----------"
        "-------------------------------------------------------------------"
        "-------+-------+----------+----------+\n| Long Amazon name because "
        "sellers like to fit as manywords into the name as possible | 98.53 "
        "|    7     |    5     |\n|                             Slightly sho"
        "rter Amazon name                            | 56.42 |    1     |   "
        " 2     |\n+--------------------------------------------------------"
        "-----------------------------+-------+----------+----------+"

        self.assertEqual(awt.prettify(wishlist), expected_result)

    def test_prettifying_empty_failure(self):
        wishlist = [{
            "name": None,
            "price": None,
            "quantity": None,
            "priority": None}
        ]

        empty_possibilities = [None, False, "", "\n"]

        for value in empty_possibilities:
            for key in wishlist[0].keys():
                wishlist[0][key] = value

            self.assertRaises(RuntimeError, awt.prettify, wishlist)
