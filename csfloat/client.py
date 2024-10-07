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

import logging
from typing import List, Optional

from .errors import BadArgument
from .http import HTTPClient
from .item import Item
from .iterators import ListingAsyncIterator
from .listing import Listing
from .user import AuthenticatedUser, User

__all__ = ("Client",)


_log = logging.getLogger(__name__)


class Client:
    def __init__(self, debug: bool = False):
        self.http: HTTPClient = HTTPClient()

    def set_api_key(self, *, api_key: str):
        self.http.set_api_key(api_key)

    async def close(self) -> None:
        """*coroutine*
        Closes the `aiohttp.ClientSession`.
        """
        await self.http.close()

    async def fetch_all_listings(self) -> ListingAsyncIterator:
        """*coroutine*
        Returns an AsyncIterator that iterates over **all** listings of csfloat.


        Returns
        -------
        :class:`ListingAsyncIterator` of :class:`Listing`
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

    async def me(self) -> AuthenticatedUser:
        """*coroutine*
        Returns the authenticated user.

        Returns
        -------
        :class:`AuthenticatedUser`
        """
        data = await self.http.me()
        return AuthenticatedUser(data=data["user"])

    async def get_inventory(self) -> List[Item]:
        """*coroutine*
        Return a list of the items in the user's inventory.

        Returns
        -------
        :class:`List` of :class:`Item`
        """
        data = await self.http.get_inventory()
        return [Item(data=item_data) for item_data in data]

    async def list_item_as_buy_now(
        self,
        asset_id: str | int,
        price: int,
        *,
        max_offer_discount: Optional[int] = None,
        description: Optional[str] = "",
        private: bool = False
    ) -> Listing:
        if isinstance(description, str) and len(description) > 32:
            raise BadArgument("description can't be longer than 32 characters")

        params = {
            "type": "buy_now",
            "asset_id": asset_id,
            "price": price,
            "private": private,
        }

        if max_offer_discount is not None:
            params["max_offer_discount"] = max_offer_discount

        if description != "":
            params["description"] = description

        data = await self.http.list_item(parameters=params)
        return Listing(data=data)

    async def list_item_as_auction(
        self, asset_id: str | int, price: int, duration_days: int, *, description: Optional[str] = "", private: bool = False
    ) -> Listing:
        if duration_days not in [1, 3, 5, 7, 14]:
            raise BadArgument("duration_days has to be a value of 1, 3, 5, 7 or 14")

        if isinstance(description, str) and len(description) > 32:
            raise BadArgument("description can't be longer than 32 characters")

        params = {
            "type": "auction",
            "asset_id": asset_id,
            "reserve_price": price,
            "duration_days": duration_days,
            "private": private,
        }

        if description != "":
            params["description"] = description

        data = await self.http.list_item(parameters=params)
        return Listing(data=data)

    async def unlist_item(self, listing_id: int):
        data = await self.http.unlist_item(listing_id=listing_id)
        return data
