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

import asyncio
import logging
from typing import List

from .http import HTTPClient
from .iterators import ListingAsyncIterator
from .listing import Listing


__all__ = ("Client",)


_log = logging.getLogger(__name__)


class Client:
    def __init__(self, debug: bool = False):
        self.http: HTTPClient = HTTPClient()

    async def close(self) -> None:
        """*coroutine*
        Closes the `aiohttp.ClientSession`.
        """
        await self.http.close()

    async def fetch_all_listings(self) -> ListingAsyncIterator:
        """*coroutine*
        Returns an AsyncIterator that iterates over all listings of csfloat.


        Returns
        -------
        :class:`TransactionAsyncIterator` of :class:`Item`
        """

        return ListingAsyncIterator(self.http.get_all_listings)

    async def get_listing(self, id: int) -> Listing:
        """*coroutine*
        Return a specific listing.

        Returns
        -------
        :class:`Listing`
        """
        data = await self.http.get_listing(item_id=id)
        return Listing(data=data)
