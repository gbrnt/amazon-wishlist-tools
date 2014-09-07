"""
Tests for amazon-wishlist-tools - Useful tools for your Amazon wishlist
"""

import unittest
import get_wishlist


class TestGetWishlist(unittest.TestCase):
    class TestArgs:
        def __init__(self, params):
            self.reveal = params["reveal"]
            self.sort = params["sort"]
            self.total = params["total"]
            self.url = params["url"]

    def setUp(self):
        params = {
            "reveal": "all",
            "sort": "last-updated",
            "total": False,
            "url": "http://amazon.co.uk/registry/wishlist/1DLH8E0VPZ6UN"
            }

        self.args = self.TestArgs(params)

    def test_construct_url_defaults(self):
        expected_url = ("http://amazon.co.uk/registry/wishlist/1DLH8E0VPZ6UN?"
                        "reveal=all&sort=last-updated&layout=compact")
        url = get_wishlist.construct_url(self.args)

        self.assertEqual(url, expected_url)

    def test_construct_url_non_defaults(self):
        self.args.reveal = "unpurchased"
        self.args.sort = "price"

        expected_url = ("http://amazon.co.uk/registry/wishlist/1DLH8E0VPZ6UN?"
                        "reveal=unpurchased&sort=price&layout=compact")
        url = get_wishlist.construct_url(self.args)

        self.assertEqual(url, expected_url)

    def test_retrieve_html_gets_html(self):
        url = ("http://amazon.co.uk/registry/wishlist/1DLH8E0VPZ6UN?reveal=un"
               "purchased&sort=price&layout=compact")

        html = get_wishlist.retrieve(url)
        html = html.split("\n")

        self.assertEqual(html[1][:15], "<!doctype html>")

    def test_parsing(self):
        with open("tests/example_wish_list.htm", "r") as example_list:
            html = example_list.read()
            
        wish_list = get_wishlist.parse_page(html)

        self.assertEqual(
            wish_list[0]["name"],
            ("Test Driven Development (The Addison-Wesley Signature Series) by"
            "Kent Beck (Paperback)")
            )

        self.assertEqual(
            wish_list[0]["price"],
            "22.99"
            )

        self.assertEqual(wish_list[0]["quantity_want"], 1)
        
        self.assertEqual(wish_list[0]["quantity_have"], 0)

        self.assertEqual(wish_list[0]["priority"], "medium")

    def test_parsing_with_modified_args(self):
        with open("tests/example_wish_list_2.htm", "r") as example_list:
            html = example_list.read()

        wish_list = get_wishlist.parse_page(html)

        self.assertEqual(
            wish_list[1]["name"],
            ("Test-Driven Development with Python by Harry J.W. Percival"
            "(Paperback)")
            )

        self.assertEqual(
            wish_list[1]["price"],
            "18.53"
            )

        self.assertEqual(wish_list[1]["quantity_want"], 2)

        self.assertEqual(wish_list[1]["quantity_have"], 1)

        self.assertEqual(wish_list[1]["priority"], "low")

    def test_wish_list_len(self):
        with open("tests/example_wish_list.htm", "r") as example_list:
            html = example_list.read()
            
        wish_list = get_wishlist.parse_page(html)

        self.assertEqual(len(wish_list), 1)
