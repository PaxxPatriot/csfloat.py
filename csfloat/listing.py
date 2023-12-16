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

import datetime
from typing import Any, Dict

from .enums import ListingType
from .item import Item, Reference
from .user import User

__all__ = ("Listing",)


class Listing:
    """Represents a listing."""

    __slots__ = (
        "_id",
        "_created_at",
        "_type",
        "_price",
        "_state",
        "_seller",
        "_reference",
        "_item",
        "_is_seller",
        "_is_watchlisted",
        "_watchers",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._id = data.get("id", "")
        self._created_at = data.get("created_at")
        self._type = data.get("type", "")
        self._price = data.get("price", 0)
        self._state = data.get("state", "")
        self._seller = data.get("seller")
        self._reference = data.get("reference")
        self._item = data.get("item")
        self._is_seller = data.get("is_seller", False)
        self._is_watchlisted = data.get("is_watchlisted", False)
        self._watchers = data.get("watchers", 0)

    @property
    def id(self) -> str:
        """:class:`str`: Returns the ID of the item."""
        return self._id

    @property
    def created_at(self) -> datetime.datetime:
        """:class:`datetime.datetime`: Returns the created at of the item."""
        return datetime.datetime.fromisoformat(self._created_at)

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
    def is_watchlisted(self) -> bool:
        """:class:`bool`: Returns whether the item is watchlisted."""
        return self._is_watchlisted

    @property
    def watchers(self) -> int:
        """:class:`int`: Returns the number of watchers for the item."""
        return self._watchers
