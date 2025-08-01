"""
MIT License

Copyright (c) 2023-present PaxxPatriot

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

import datetime
from typing import Any, Dict, Optional

from .enums import ListingType
from .item import Item, Reference
from .user import User

__all__ = (
    "TopBid",
    "AuctionDetails",
    "Listing",
)


class TopBid:
    """Represents the top bid."""

    __slots__ = (
        "_bid_id",
        "_created_at",
        "_price",
        "_contract_id",
        "_state",
        "_obfuscated_buyer_id",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._bid_id = data.get("id", "")
        self._created_at = data.get("created_at", "1970-01-01T00:00:00.000000Z")
        self._price = data.get("price", "")
        self._contract_id = data.get("contract_id", 0)
        self._state = data.get("state", "")
        self._obfuscated_buyer_id = data.get("obfuscated_buyer_id", 0)

    def __repr__(self) -> str:
        return f"TopBid(data={{'id': {self._bid_id!r}, 'created_at': {self._created_at!r}, 'price': {self._price!r}, 'contract_id': {self._contract_id!r}, 'state': {self._state!r}, 'obfuscated_buyer_id': {self._obfuscated_buyer_id!r}}})"

    @property
    def bid_id(self) -> str:
        return self._bid_id

    @property
    def created_at(self) -> datetime.datetime:
        """:class:`datetime.datetime`: Returns the created at of the item."""
        return datetime.datetime.fromisoformat(self._created_at)

    @property
    def price(self) -> float:
        """:class:`float`: Returns the price of the item in USD."""
        return self._price / 100

    @property
    def contract_id(self) -> str:
        return self._contract_id

    @property
    def state(self) -> str:
        return self._state

    @property
    def obfuscated_buyer_id(self) -> str:
        return self._obfuscated_buyer_id


class AuctionDetails:
    """Represents the auction details."""

    __slots__ = (
        "_reserve_price",
        "_top_bid",
        "_expires_at",
        "_min_next_bid",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._reserve_price = data.get("reserve_price", 0.0)
        self._top_bid = data.get("top_bid")
        self._expires_at = data.get("expires_at", "1970-01-01T00:00:00.000000Z")
        self._min_next_bid = data.get("min_next_bid", 0.0)

    def __repr__(self) -> str:
        return f"AuctionDetails(data={{'reserve_price': {self._reserve_price!r}, 'top_bid': {self._top_bid!r}, 'expires_at': {self._expires_at!r}, 'min_next_bid': {self._min_next_bid!r}}})"

    @property
    def reserve_price(self) -> float:
        return self._reserve_price / 100

    @property
    def top_bid(self) -> TopBid:
        return TopBid(data=self._top_bid)

    @property
    def expires_at(self) -> datetime.datetime:
        return datetime.datetime.fromisoformat(self._expires_at)

    @property
    def min_next_bid(self) -> float:
        return self._min_next_bid / 100


class Listing:
    """Represents a listing."""

    __slots__ = (
        "_listing_id",
        "_created_at",
        "_description",
        "_type",
        "_price",
        "_state",
        "_seller",
        "_reference",
        "_item",
        "_is_seller",
        "_min_offer_price",
        "_max_offer_discount",
        "_is_watchlisted",
        "_watchers",
        "_auction_details",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._listing_id = data.get("id", "")
        self._created_at = data.get("created_at", "1970-01-01T00:00:00.000000Z")
        self._description = data.get("description", None)
        self._type = data.get("type", "")
        self._price = data.get("price", 0)
        self._state = data.get("state", "")
        self._seller = data.get("seller")
        self._reference = data.get("reference")
        self._item = data.get("item")
        self._is_seller = data.get("is_seller", False)
        self._min_offer_price = data.get("min_offer_price", None)
        self._max_offer_discount = data.get("max_offer_discount", None)
        self._is_watchlisted = data.get("is_watchlisted", False)
        self._watchers = data.get("watchers", 0)
        self._auction_details = data.get("auction_details", None)

    def __repr__(self) -> str:
        return f"Listing(data={{'id': {self._listing_id!r}, 'created_at': {self._created_at!r},  'description': {self._description!r}, 'type': {self._type!r}, 'price': {self._price!r}, 'state': {self._state!r}, 'seller': {self._seller!r}, 'reference': {self._reference!r}, 'item': {self._item!r}, 'is_seller': {self._is_seller!r}, 'min_offer_price': {self._min_offer_price!r}, 'max_offer_discount': {self._max_offer_discount!r}, 'is_watchlisted': {self._is_watchlisted!r}, 'watchers': {self._watchers!r}, 'auction_details': {self._auction_details!r}}})"

    @property
    def listing_id(self) -> str:
        """:class:`str`: Returns the ID of the item."""
        return self._listing_id

    @property
    def created_at(self) -> datetime.datetime:
        """:class:`datetime.datetime`: Returns the created at of the item."""
        return datetime.datetime.fromisoformat(self._created_at)

    @property
    def description(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the description of the listing."""
        return self._description

    @property
    def type(self) -> ListingType:
        """:class:`ListingType`: Returns the type of listing of the item."""
        return ListingType(self._type)

    @property
    def price(self) -> float:
        """:class:`float`: Returns the price of the item in USD."""
        return self._price / 100

    @property
    def state(self) -> str:
        """:class:`str`: Returns the state of the item."""
        return self._state

    @property
    def seller(self) -> User:
        """Returns the seller of the item."""
        return User(data=self._seller)

    @property
    def reference(self) -> Reference:
        """Returns the reference of the item."""
        return Reference(data=self._reference)

    @property
    def item(self) -> Item:
        """Returns the item."""
        return Item(data=self._item)

    @property
    def is_seller(self) -> bool:
        """:class:`bool`: Returns whether the current user is the seller of the item."""
        return self._is_seller

    @property
    def min_offer_price(self) -> Optional[float]:
        """:class:`float`: Returns the minimum price you have to offer."""
        return self._min_offer_price / 100 if self._min_offer_price else None

    @property
    def max_offer_discount(self) -> Optional[float]:
        """:class:`float`: Returns the max discount in percent."""
        return self._max_offer_discount / 10_000 if self._max_offer_discount else None

    @property
    def is_watchlisted(self) -> bool:
        """:class:`bool`: Returns whether the item is watchlisted."""
        return self._is_watchlisted

    @property
    def watchers(self) -> int:
        """:class:`int`: Returns the number of watchers for the item."""
        return self._watchers

    @property
    def auction_details(self) -> Optional[AuctionDetails]:
        """:class:`AuctionDetails`: Returns the details of the auction, if the listing is an auction."""
        return AuctionDetails(data=self._auction_details) if self._auction_details else None
