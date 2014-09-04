"""
Tests for amazon-wishlist-tools - Useful tools for your Amazon wishlist
"""

import unittest
import argparse
import arg_parser


class ParseArguments(unittest.TestCase):
    def setUp(self):
        self.parser = arg_parser.create_parser()

    def test_create_parser(self):
        self.assertIsInstance(self.parser, argparse.ArgumentParser)

    def test_parser_creates_namespace(self):
        args = self.parser.parse_args(["http://amazon.co.uk"])
        
        self.assertIsInstance(args, Namespace)

    def test_parser_defaults(self):
        args = self.parser.parse_args(["http://amazon.co.uk"])

        self.assertEqual(args.reveal, "all")
        self.assertEqual(args.sort, "last-updated")
        self.asertEqual(args.total, False)
        self.assertEqual(args.url, "http://amazon.co.uk")

    def test_parser_exception_on_no_url(self):
        """Argument parser should raise an exception [name to be found] when no URL is given"""
        self.assertRaises(ExceptionName, self.parser.parse_args)

    def test_parser_given_all_args(self):
        args_to_give = [
            "--reveal", "unpurchased",
            "--sort", "priority",
            "--total",
            "http://amazon.co.uk"
        ]

        args = self.parser.parse_args(args_to_give))

        self.assertEqual(args.reveal, "unpurchased")
        self.assertEqual(args.sort, "priority")
        self.assertEqual(args.total, True)
        self.assertEqual(args.url, "http://amazon.co.uk")
