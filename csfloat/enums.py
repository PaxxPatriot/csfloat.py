"""
MIT License

Copyright (c) 2023 PaxxPatriot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from enum import Enum, IntEnum

__all__ = (
    "SortingParameter",
    "Category",
    "ListingType",
)


class SortingParameter(Enum):
    lowest_price = "lowest_price"
    highest_price = "highest_price"
    most_recent = "most_recent"
    expires_soon = "expires_soon"
    lowest_float = "lowest_float"
    highest_float = "highest_float"
    best_deal = "best_deal"
    highest_discount = "highest_discount"
    float_rank = "float_rank"
    num_bids = "num_bids"

    def __str__(self) -> str:
        return self.value


class Category(IntEnum):
    any = 0
    normal = 1
    stattrak = 2
    souvenir = 3


class ListingType(Enum):
    buy_now = "buy_now"
    auction = "auction"
