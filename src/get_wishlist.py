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

import bs4
import requests

"""
def get(args):
    url = construct_url(args)
    page = retrieve(url)
    wishlist = parse_page(page)
    return wishlist

def construct_url(args):
    Add necessary arguments onto url
    http://www.artiss.co.uk/2012/10/how-to-sequence-a-shared-amazon-wish-list
    return url

def retrieve(url):
    Get page from amazon
    # page_html = requests.get(url).text
    return page_html

def parse_page(page):
    Use beautifulsoup to get necessary parts of page:
        Name, price, num(wanted-got), priority
    Make these into list of dicts - each dict being an item on the list
    wishlist_dict{
        name:, price:, quantity_want:, quantity_have:, priority:
    }
    return wishlist_dict
"""
