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
from typing import Any, Dict, Optional

__all__ = (
    "Reference",
    "Item",
)


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


class Item:
    __slots__ = (
        "_asset_id",
        "_def_index",
        "_paint_index",
        "_paint_seed",
        "_float_value",
        "_icon_url",
        "_d_param",
        "_is_stattrak",
        "_is_souvenir",
        "_rarity",
        "_quality",
        "_market_hash_name",
        "_stickers",
        "_tradable",
        "_inspect_link",
        "_has_screenshot",
        "_is_commodity",
        "_type",
        "_rarity_name",
        "_type_name",
        "_item_name",
        "_wear_name",
        "_description",
        "_collection",
        "_reference",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._asset_id = data.get("asset_id", "")
        self._def_index = data.get("def_index", 0)
        self._paint_index = data.get("paint_index", 0)
        self._paint_seed = data.get("paint_seed", 0)
        self._float_value = data.get("float_value")
        self._icon_url = data.get("icon_url", "")
        self._d_param = data.get("d_param", "")
        self._is_stattrak = data.get("is_stattrak", False)
        self._is_souvenir = data.get("is_souvenir", False)
        self._rarity = data.get("rarity", 0)
        self._quality = data.get("quality", 0)
        self._market_hash_name = data.get("market_hash_name")
        self._stickers = data.get("stickers", [])
        self._tradable = data.get("tradable", False)
        self._inspect_link = data.get("inspect_link")
        self._has_screenshot = data.get("has_screenshot", False)
        self._is_commodity = data.get("is_commodity")
        self._type = data.get("type", "")
        self._rarity_name = data.get("rarity_name", "")
        self._type_name = data.get("type_name", "")
        self._item_name = data.get("item_name", "")
        self._wear_name = data.get("wear_name", "")
        self._description = data.get("description", "")
        self._collection = data.get("collection", "")
        self._reference = data.get("reference")

    @property
    def asset_id(self) -> Any:
        """:class:`Any`: Returns the asset ID of the item."""
        return self._asset_id

    @property
    def def_index(self) -> Any:
        """:class:`Any`: Returns the def index of the item."""
        return self._def_index

    @property
    def paint_index(self) -> Any:
        """:class:`Any`: Returns the paint index of the item."""
        return self._paint_index

    @property
    def paint_seed(self) -> Any:
        """:class:`Any`: Returns the paint seed of the item."""
        return self._paint_seed

    @property
    def float_value(self) -> Optional[float]:
        """:class:`Any`: Returns the float value of the item."""
        return self._float_value

    @property
    def icon_url(self) -> Any:
        """:class:`Any`: Returns the icon URL of the item."""
        return self._icon_url

    @property
    def d_param(self) -> Any:
        """:class:`Any`: Returns the d param of the item."""
        return self._d_param

    @property
    def is_stattrak(self) -> Any:
        """:class:`Any`: Returns the stattrak status of the item."""
        return self._is_stattrak

    @property
    def is_souvenir(self) -> Any:
        """:class:`Any`: Returns the souvenir status of the item."""
        return self._is_souvenir

    @property
    def rarity(self) -> Any:
        """:class:`Any`: Returns the rarity of the item."""
        return self._rarity

    @property
    def quality(self) -> Any:
        """:class:`Any`: Returns the quality of the item."""
        return self._quality

    @property
    def market_hash_name(self) -> Any:
        """:class:`Any`: Returns the market hash name of the item."""
        return self._market_hash_name

    @property
    def stickers(self) -> Any:
        """:class:`Any`: Returns the stickers of the item."""
        return self._stickers

    @property
    def tradable(self) -> Any:
        """:class:`Any`: Returns the tradable status of the item."""
        return self._tradable

    @property
    def inspect_link(self) -> Any:
        """:class:`Any`: Returns the inspect link of the item."""
        return self._inspect_link

    @property
    def has_screenshot(self) -> Any:
        """:class:`Any`: Returns the screenshot status of the item."""
        return self._has_screenshot

    @property
    def is_commodity(self) -> Any:
        """:class:`Any`: Returns the commodity status of the item."""
        return self._is_commodity

    @property
    def type(self) -> Any:
        """:class:`Any`: Returns the type of the item."""
        return self._type

    @property
    def rarity_name(self) -> Any:
        """:class:`Any`: Returns the rarity name of the item."""
        return self._rarity_name

    @property
    def type_name(self) -> Any:
        """:class:`Any`: Returns the type name of the item."""
        return self._type_name

    @property
    def item_name(self) -> Any:
        """:class:`Any`: Returns the item name of the item."""
        return self._item_name

    @property
    def wear_name(self) -> Any:
        """:class:`Any`: Returns the wear name of the item."""
        return self._wear_name

    @property
    def description(self) -> Any:
        """:class:`Any`: Returns the description of the item."""
        return self._description

    @property
    def collection(self) -> Any:
        """:class:`Any`: Returns the collection of the item."""
        return self._collection

    @property
    def reference(self) -> Any:
        """:class:`Any`: Returns the reference of the item."""
        return self._reference
