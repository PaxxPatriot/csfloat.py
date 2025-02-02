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
from typing import Any, Dict, List, Optional
from .enums import Rarity

__all__ = (
    "FadeInfo",
    "StickerReference",
    "Reference",
    "Sticker",
    "Item",
)


class FadeInfo:
    __slots__ = (
        "_seed",
        "_percentage",
        "_rank",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._seed = data.get("seed")
        self._percentage = data.get("percentage")
        self._rank = data.get("rank")

    def __repr__(self) -> str:
        return f"FadeInfo({{'seed': {self._seed}, 'percentage': {self._percentage}, 'rank': {self._rank}}})"

    @property
    def seed(self) -> int:
        return self._seed

    @property
    def percentage(self) -> float:
        return self._percentage

    @property
    def rank(self) -> int:
        return self._rank


class StickerReference:
    __slots__ = (
        "_price",
        "_quantity",
        "_updated_at",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._price = data.get("price", 0)
        self._quantity = data.get("quantity", 0)
        self._updated_at = data.get("updated_at", "1970-01-01T00:00:00.000000Z")

    def __repr__(self) -> str:
        return f"StickerReference({{'price': {self._price}, 'quantity': {self._quantity}, 'updated_at': {self._updated_at}}})"

    @property
    def price(self) -> float:
        return self._price / 100

    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def updated_at(self) -> datetime.datetime:
        return datetime.datetime.fromisoformat(self._updated_at)


class Reference:
    __slots__ = (
        "_base_price",
        "_float_factor",
        "_predicted_price",
        "_quantity",
        "_last_updated",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._base_price = data.get("base_price", 0)
        self._float_factor = data.get("float_factor", 1.0)
        self._predicted_price = data.get("predicted_price", 0)
        self._quantity = data.get("quantity", 0)
        self._last_updated = data.get("last_updated", "1970-01-01T00:00:00.000000Z")

    def __repr__(self) -> str:
        return f"Reference({{'base_price': {self._base_price}, 'float_factor': {self._float_factor}, 'predicted_price': {self._predicted_price}, 'quantity': {self._quantity}, 'last_updated': {self._last_updated}}})"

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


class Sticker:
    __slots__ = (
        "_sticker_id",
        "_slot",
        "_wear",
        "_icon_url",
        "_name",
        "_reference",
        "_offset_x",
        "_offset_y",
        "_rotation",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._sticker_id = data.get("stickerId", 0)
        self._slot = data.get("slot", 0)
        self._wear = data.get("wear", 1.0)
        self._icon_url = data.get("icon_url", "")
        self._name = data.get("name", "")
        self._reference = data.get("reference")
        self._offset_x = data.get("offset_x")
        self._offset_y = data.get("offset_y")
        self._rotation = data.get("rotation")

    def __repr__(self) -> str:
        return f"Sticker({{'stickerId': {self._sticker_id}, 'slot': {self._slot}, 'wear': {self._wear}, 'icon_url': {self._icon_url}, 'name': {self._name}, 'reference': {self._reference}, 'offset_x': {self._offset_x}, 'offset_y': {self._offset_y}, 'rotation': {self._rotation}}})"

    @property
    def sticker_id(self) -> int:
        return self._sticker_id

    @property
    def slot(self) -> int:
        return self._slot

    @property
    def wear(self) -> float:
        return self._wear

    @property
    def icon_url(self) -> str:
        return self._icon_url

    @property
    def name(self) -> str:
        return self._name

    @property
    def reference(self) -> Optional[StickerReference]:
        return StickerReference(data=self._reference) if self._reference else None

    @property
    def offset_x(self) -> float:
        return self._offset_x

    @property
    def offset_y(self) -> float:
        return self._offset_y

    @property
    def rotation(self) -> int:
        return self._rotation


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
        "_low_rank",
        "_tradable",
        "_inspect_link",
        "_has_screenshot",
        "_cs2_screenshot_id",
        "_cs2_screenshot_at",
        "_is_commodity",
        "_type",
        "_rarity_name",
        "_type_name",
        "_item_name",
        "_wear_name",
        "_description",
        "_collection",
        "_serialized_inspect",
        "_gs_sig",
        "_high_rank",
        "_phase",
        "_sticker_index",
        "_badges",
        "_fade",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._asset_id = data.get("asset_id", "")
        self._def_index = data.get("def_index", 0)
        self._paint_index = data.get("paint_index", 0)
        self._paint_seed = data.get("paint_seed", 0)
        self._float_value = data.get("float_value", 0.0)
        self._icon_url = data.get("icon_url", "")
        self._d_param = data.get("d_param", "")
        self._is_stattrak = data.get("is_stattrak", False)
        self._is_souvenir = data.get("is_souvenir", False)
        self._rarity = data.get("rarity", 0)
        self._quality = data.get("quality", 0)
        self._market_hash_name = data.get("market_hash_name")
        self._stickers = data.get("stickers", [])
        self._low_rank = data.get("low_rank", 1_000_000)
        self._tradable = data.get("tradable", False)
        self._inspect_link = data.get("inspect_link", None)
        self._has_screenshot = data.get("has_screenshot", False)
        self._cs2_screenshot_id = data.get("cs2_screenshot_id", "")
        self._cs2_screenshot_at = data.get("cs2_screenshot_at", "1970-01-01T00:00:00.000000Z")
        self._is_commodity = data.get("is_commodity", False)
        self._type = data.get("type", "")
        self._rarity_name = data.get("rarity_name", "")
        self._type_name = data.get("type_name", "")
        self._item_name = data.get("item_name", "")
        self._wear_name = data.get("wear_name", "")
        self._description = data.get("description", "")
        self._collection = data.get("collection", "")
        self._serialized_inspect = data.get("serialized_inspect", "")
        self._gs_sig = data.get("gs_sig", "")
        self._high_rank = data.get("high_rank", None)
        self._phase = data.get("phase", None)
        self._sticker_index = data.get("sticker_index", None)
        self._badges = data.get("badges", [])
        self._fade = data.get("fade", None)

    @property
    def asset_id(self) -> str:
        """:class:`str`: Returns the asset ID of the item."""
        return self._asset_id

    @property
    def def_index(self) -> int:
        """:class:`int`: Returns the def index of the item."""
        return self._def_index

    @property
    def paint_index(self) -> int:
        """:class:`int`: Returns the paint index of the item."""
        return self._paint_index

    @property
    def paint_seed(self) -> int:
        """:class:`int`: Returns the paint seed of the item."""
        return self._paint_seed

    @property
    def float_value(self) -> Optional[float]:
        """:class:`Any`: Returns the float value of the item."""
        return self._float_value

    @property
    def icon_url(self) -> str:
        """:class:`str`: Returns the icon URL of the item."""
        return f"https://community.cloudflare.steamstatic.com/economy/image/{self._icon_url}"

    @property
    def d_param(self) -> str:
        """:class:`str`: Returns the d param of the item."""
        return self._d_param

    @property
    def is_stattrak(self) -> bool:
        """:class:`bool`: Returns the stattrak status of the item."""
        return self._is_stattrak

    @property
    def is_souvenir(self) -> bool:
        """:class:`bool`: Returns the souvenir status of the item."""
        return self._is_souvenir

    @property
    def rarity(self) -> Rarity:
        """:class:`Rarity`: Returns the rarity of the item."""
        return Rarity(self._rarity)

    @property
    def quality(self) -> int:
        """:class:`int`: Returns the quality of the item."""
        return self._quality

    @property
    def market_hash_name(self) -> str:
        """:class:`str`: Returns the market hash name of the item."""
        return self._market_hash_name

    @property
    def stickers(self) -> List[Sticker]:
        """:class:`List` of :class:`Sticker`: Returns the stickers of the item."""
        return [Sticker(data=sticker) for sticker in self._stickers]

    @property
    def low_rank(self) -> int:
        """:class:`int`: Returns the rank in FloatDB of the item."""
        return self._low_rank

    @property
    def tradable(self) -> int:
        """:class:`int`: Returns the tradable status of the item."""
        return self._tradable

    @property
    def inspect_link(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the inspect link of the item."""
        return self._inspect_link

    @property
    def has_screenshot(self) -> bool:
        """:class:`bool`: Returns the screenshot status of the item."""
        return self._has_screenshot

    @property
    def cs2_screenshot_id(self) -> str:
        """:class:`str`: Returns the CS2 screenshot ID."""
        return self._cs2_screenshot_id

    @property
    def cs2_screenshot_at(self) -> datetime.datetime:
        """:class:`datetime.datetime`: Returns timestamp of when the CS2 screenshot was taken."""
        return datetime.datetime.fromisoformat(self._cs2_screenshot_at)

    @property
    def is_commodity(self) -> bool:
        """:class:`bool`: Returns the commodity status of the item."""
        return self._is_commodity

    @property
    def type(self) -> str:
        """:class:`str`: Returns the type of the item."""
        return self._type

    @property
    def rarity_name(self) -> str:
        """:class:`str`: Returns the rarity name of the item."""
        return self._rarity_name

    @property
    def type_name(self) -> str:
        """:class:`str`: Returns the type name of the item."""
        return self._type_name

    @property
    def item_name(self) -> str:
        """:class:`str`: Returns the item name of the item."""
        return self._item_name

    @property
    def wear_name(self) -> str:
        """:class:`str`: Returns the wear name of the item."""
        return self._wear_name

    @property
    def description(self) -> str:
        """:class:`str`: Returns the description of the item."""
        return self._description

    @property
    def collection(self) -> str:
        """:class:`str`: Returns the collection of the item."""
        return self._collection

    @property
    def serialized_inspect(self) -> str:
        return self._serialized_inspect

    @property
    def gs_sig(self) -> str:
        return self._gs_sig

    @property
    def high_rank(self) -> Optional[int]:
        """Optional[:class:`int`]: Returns the rank in the CSFloat float database."""
        return self._high_rank

    @property
    def phase(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the Doppler or Gamma Doppler phase of the item."""
        return self._phase

    @property
    def sticker_index(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the index if the item is a sticker."""
        return self._sticker_index

    @property
    def badges(self) -> List[str]:
        """List[:class:`str`]: Returns a list of badges."""
        return self._badges

    @property
    def fade(self) -> Optional[FadeInfo]:
        return FadeInfo(data=self._fade) if self._fade is not None else None
