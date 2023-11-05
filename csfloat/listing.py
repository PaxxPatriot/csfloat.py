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
from typing import Any, Dict, NamedTuple, Optional

from .enums import ListingType

__all__ = (
    "SteamCommunityMarket",
    "Reference",
    "Seller",
    "Statistics",
    "Item",
    "Listing",
)


class SteamCommunityMarket(NamedTuple):
    price: int
    volume: int


class Reference:
    __slots__ = (
        "_base_price",
        "_predicted_price",
        "_quantity",
        "_last_updated",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._base_price = data.get("base_price", 0)
        self._predicted_price = data.get("predicted_price", 0)
        self._quantity = data.get("quantity", 0)
        self._last_updated = data.get("last_updated")

    @property
    def base_price(self) -> float:
        """:class:`float`: Returns the base price of the reference."""
        return self._base_price / 100

    @property
    def predicted_price(self) -> float:
        """:class:`float`: Returns the predicted price of the reference."""
        return self._predicted_price / 100

    @property
    def quantity(self) -> int:
        """:class:`int`: Returns the quantity of the reference."""
        return self._quantity

    @property
    def last_updated(self) -> datetime.datetime:
        """:class:`datetime.datetime`: Returns the last updated timestamp of the reference."""
        return datetime.datetime.fromisoformat(self._last_updated)


class Statistics:
    __slots__ = (
        "_median_trade_time",
        "_total_avoided_trades",
        "_total_failed_trades",
        "_total_trades",
        "_total_verified_trades",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._median_trade_time = data.get("median_trade_time", 0)
        self._total_avoided_trades = data.get("total_avoided_trades", 0)
        self._total_failed_trades = data.get("total_failed_trades", 0)
        self._total_trades = data.get("total_trades", 0)
        self._total_verified_trades = data.get("total_verified_trades", 0)

    @property
    def median_trade_time(self) -> int:
        """:class:`int`: Returns the median trade time of the seller in seconds."""
        return self._median_trade_time

    @property
    def total_avoided_trades(self) -> int:
        """:class:`int`: Returns the number of avoided trades of the seller."""
        return self._total_avoided_trades

    @property
    def total_failed_trades(self) -> int:
        """:class:`int`: Returns the number of failed trades of the seller."""
        return self._total_failed_trades

    @property
    def total_trades(self) -> int:
        """:class:`int`: Returns the number of trades of the seller."""
        return self._total_trades

    @property
    def total_verified_trades(self) -> int:
        """:class:`int`: Returns the number of verified trades of the seller."""
        return self._total_verified_trades


class Seller:
    __slots__ = (
        "_avatar",
        "_away",
        "_flags",
        "_has_valid_steam_api_key",
        "_online",
        "_stall_public",
        "_statistics",
        "_steam_id",
        "_username",
        "_verification_mode",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._avatar = data.get("avatar")
        self._away = data.get("away", False)
        self._flags = data.get("flags")
        self._has_valid_steam_api_key = data.get("has_valid_steam_api_key", False)
        self._online = data.get("online", False)
        self._stall_public = data.get("stall_public", False)
        self._statistics = data.get("statistics")
        self._steam_id = data.get("steam_id")
        self._username = data.get("username")
        self._verification_mode = data.get("verification_mode")

    @property
    def avatar(self) -> str:
        """:class:`str`: Returns the URL to the avatar of the seller."""
        return self._avatar

    @property
    def away(self) -> bool:
        """:class:`bool`: Returns the away status of the seller."""
        return self._away

    @property
    def flags(self) -> int:
        """:class:`int`: Returns the flags of the seller."""
        return self._flags

    @property
    def has_valid_steam_api_key(self) -> bool:
        """:class:`bool`: Returns the validity of the Steam API key of the seller."""
        return self._has_valid_steam_api_key

    @property
    def online(self) -> bool:
        """:class:`bool`: Returns the online status of the seller."""
        return self._online

    @property
    def stall_public(self) -> bool:
        """:class:`bool`: Returns the public stall status of the seller."""
        return self._stall_public

    @property
    def statistics(self) -> Statistics:
        """:class:`Any`: Returns the statistics of the seller."""
        return Statistics(data=self._statistics)

    @property
    def steam_id(self) -> Optional[str]:
        """:class:`str`: Returns the Steam ID of the seller."""
        return self._steam_id

    @property
    def username(self) -> Optional[str]:
        """:class:`str`: Returns the username of the seller."""
        return self._username

    @property
    def verification_mode(self) -> str:
        """:class:`str`: Returns the verification mode of the seller."""
        return self._verification_mode


class Item:
    __slots__ = (
        "_asset_id",
        "_def_index",
        "_sticker_index",
        "_icon_url",
        "_rarity",
        "_market_hash_name",
        "_tradable",
        "_inspect_link",
        "_has_screenshot",
        "_is_commodity",
        "_type",
        "_scm",
        "_rarity_name",
        "_type_name",
        "_item_name",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._asset_id = data.get("asset_id")
        self._def_index = data.get("def_index", 0)
        self._sticker_index = data.get("sticker_index", 0)
        self._icon_url = data.get("icon_url")
        self._rarity = data.get("rarity", 0)
        self._market_hash_name = data.get("market_hash_name")
        self._tradable = data.get("tradable", False)
        self._inspect_link = data.get("inspect_link")
        self._has_screenshot = data.get("has_screenshot", False)
        self._is_commodity = data.get("is_commodity")
        self._type = data.get("type")
        self._scm = data.get("scm")
        self._rarity_name = data.get("rarity_name")
        self._type_name = data.get("type_name")
        self._item_name = data.get("item_name")

    @property
    def asset_id(self) -> str:
        return self._asset_id

    @property
    def def_index(self) -> int:
        return self._def_index

    @property
    def sticker_index(self) -> int:
        return self._sticker_index

    @property
    def icon_url(self) -> str:
        return f"https://community.cloudflare.steamstatic.com/economy/image/{self._icon_url}"

    @property
    def rarity(self) -> int:
        return self._rarity

    @property
    def market_hash_name(self) -> str:
        return self._market_hash_name

    @property
    def tradable(self) -> int:
        return self._tradable

    @property
    def inspect_link(self) -> str:
        return self._inspect_link

    @property
    def has_screenshot(self) -> bool:
        return self._has_screenshot

    @property
    def is_commodity(self) -> bool:
        return self._is_commodity

    @property
    def type(self) -> str:
        return self._type

    @property
    def scm(self) -> Optional[SteamCommunityMarket]:
        return SteamCommunityMarket(**self._scm) if self._scm else None

    @property
    def rarity_name(self) -> str:
        return self._rarity_name

    @property
    def type_name(self) -> str:
        return self._type_name

    @property
    def item_name(self) -> str:
        return self._item_name


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
    def seller(self) -> Seller:
        """Returns the seller of the item."""
        return Seller(data=self._seller)

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
