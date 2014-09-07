"""
Amazon-wishlist-tools - Useful tools for your Amazon wishlist

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description="Useful tools for your Amazon wishlist")

    parser.add_argument("-r", "--reveal",
                        choices=["all", "purchased", "unpurchased"],
                        default="all",
                        help=("Reveal all items or only "
                              "those purchased or unpurchased"))

    sort_choices = ["priority", "last-updated", "date-added",
                    "price", "price-desc", "name"]
    parser.add_argument("-s", "--sort",
                        choices=sort_choices,
                        default="last-updated",
                        help="Choose sorting method")

    parser.add_argument("-t", "--total",
                        action="store_true",
                        default=False,
                        help="Shows total cost")

    parser.add_argument("url",
                        help="The URL of the amazon wish list to use")

    return parser
