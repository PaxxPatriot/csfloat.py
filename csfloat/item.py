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
    "AttachmentReference",
    "Reference",
    "Keychain",
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
        return f"FadeInfo(data={{'seed': {self._seed!r}, 'percentage': {self._percentage!r}, 'rank': {self._rank!r}}})"

    @property
    def seed(self) -> int:
        return self._seed

    @property
    def percentage(self) -> float:
        return self._percentage

    @property
    def rank(self) -> int:
        return self._rank


class AttachmentReference:
    __slots__ = (
        "_price",
        "_quantity",
        "_updated_at",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._price = data.get("price")
        self._quantity = data.get("quantity")
        self._updated_at = data.get("updated_at", "1970-01-01T00:00:00.000000Z")

    def __repr__(self) -> str:
        return f"AttachmentReference(data={{'price': {self._price!r}, 'quantity': {self._quantity!r}, 'updated_at': {self._updated_at!r}}})"

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
        self._base_price = data.get("base_price")
        self._float_factor = data.get("float_factor", 1.0)
        self._predicted_price = data.get("predicted_price")
        self._quantity = data.get("quantity")
        self._last_updated = data.get("last_updated", "1970-01-01T00:00:00.000000Z")

    def __repr__(self) -> str:
        return f"Reference(data={{'base_price': {self._base_price!r}, 'float_factor': {self._float_factor!r}, 'predicted_price': {self._predicted_price!r}, 'quantity': {self._quantity!r}, 'last_updated': {self._last_updated!r}}})"

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


class Keychain:
    __slots__ = (
        "_sticker_id",
        "_slot",
        "_offset_x",
        "_offset_y",
        "_offset_z",
        "_pattern",
        "_icon_url",
        "_name",
        "_reference",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._sticker_id = data.get("stickerId")
        self._slot = data.get("slot")
        self._offset_x = data.get("offset_x")
        self._offset_y = data.get("offset_y")
        self._offset_z = data.get("offset_z")
        self._pattern = data.get("pattern")
        self._icon_url = data.get("icon_url")
        self._name = data.get("name")
        self._reference = data.get("reference")

    def __repr__(self) -> str:
        return f"Keychain(data={{'stickerId': {self._sticker_id!r}, 'slot': {self._slot!r}, 'offset_x': {self._offset_x!r}, 'offset_y': {self._offset_y!r}, 'offset_z': {self._offset_z!r}, 'pattern': {self._pattern!r}, 'icon_url': {self._icon_url!r}, 'name': {self._name!r}, 'reference': {self._reference!r}}})"

    @property
    def sticker_id(self) -> int:
        return self._sticker_id

    @property
    def slot(self) -> int:
        return self._slot

    @property
    def offset_x(self) -> float:
        return self._offset_x

    @property
    def offset_y(self) -> float:
        return self._offset_y

    @property
    def offset_z(self) -> float:
        return self._offset_z

    @property
    def pattern(self) -> float:
        return self._pattern

    @property
    def icon_url(self) -> str:
        return self._icon_url

    @property
    def name(self) -> str:
        return self._name

    @property
    def reference(self) -> Optional[AttachmentReference]:
        return AttachmentReference(data=self._reference) if self._reference else None


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
        self._sticker_id = data.get("stickerId")
        self._slot = data.get("slot")
        self._wear = data.get("wear", 1.0) 
        self._icon_url = data.get("icon_url")
        self._name = data.get("name")
        self._reference = data.get("reference")
        self._offset_x = data.get("offset_x")
        self._offset_y = data.get("offset_y")
        self._rotation = data.get("rotation")

    def __repr__(self) -> str:
        return f"Sticker(data={{'stickerId': {self._sticker_id!r}, 'slot': {self._slot!r}, 'wear': {self._wear!r}, 'icon_url': {self._icon_url!r}, 'name': {self._name!r}, 'reference': {self._reference!r}, 'offset_x': {self._offset_x!r}, 'offset_y': {self._offset_y!r}, 'rotation': {self._rotation!r}}})"

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
    def reference(self) -> Optional[AttachmentReference]:
        return AttachmentReference(data=self._reference) if self._reference else None

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
        "_keychains",
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
        self._asset_id = data.get("asset_id")
        self._def_index = data.get("def_index")
        self._paint_index = data.get("paint_index")
        self._paint_seed = data.get("paint_seed")
        self._float_value = data.get("float_value")
        self._icon_url = data.get("icon_url")
        self._d_param = data.get("d_param")
        self._is_stattrak = data.get("is_stattrak")
        self._is_souvenir = data.get("is_souvenir")
        self._rarity = data.get("rarity")
        self._quality = data.get("quality")
        self._market_hash_name = data.get("market_hash_name")
        self._stickers = data.get("stickers")
        self._keychains = data.get("keychains")
        self._low_rank = data.get("low_rank")
        self._tradable = data.get("tradable")
        self._inspect_link = data.get("inspect_link")
        self._has_screenshot = data.get("has_screenshot")
        self._cs2_screenshot_id = data.get("cs2_screenshot_id")
        self._cs2_screenshot_at = data.get("cs2_screenshot_at")
        self._is_commodity = data.get("is_commodity")
        self._type = data.get("type")
        self._rarity_name = data.get("rarity_name")
        self._type_name = data.get("type_name")
        self._item_name = data.get("item_name")
        self._wear_name = data.get("wear_name")
        self._description = data.get("description")
        self._collection = data.get("collection")
        self._serialized_inspect = data.get("serialized_inspect")
        self._gs_sig = data.get("gs_sig")
        self._high_rank = data.get("high_rank")
        self._phase = data.get("phase")
        self._sticker_index = data.get("sticker_index")
        self._badges = data.get("badges")
        self._fade = data.get("fade")

    def __repr__(self) -> str:
        return f"Item(data={{'asset_id': {self._asset_id!r}, 'def_index': {self._def_index!r}, 'paint_index': {self._paint_index!r}, 'paint_seed': {self._paint_seed!r}, 'float_value': {self._float_value!r}, 'icon_url': {self._icon_url!r}, 'd_param': {self._d_param!r}, 'is_stattrak': {self._is_stattrak!r}, 'is_souvenir': {self._is_souvenir!r}, 'rarity': {self._rarity!r}, 'quality': {self._quality!r}, 'market_hash_name': {self._market_hash_name!r}, 'stickers': {self._stickers!r}, 'keychains': {self._keychains!r}, 'low_rank': {self._low_rank!r}, 'tradable': {self._tradable!r}, 'inspect_link': {self._inspect_link!r}, 'has_screenshot': {self._has_screenshot!r}, 'cs2_screenshot_id': {self._cs2_screenshot_id!r}, 'cs2_screenshot_at': {self._cs2_screenshot_at!r}, 'is_commodity': {self._is_commodity!r}, 'type': {self._type!r}, 'rarity_name': {self._rarity_name!r}, 'type_name': {self._type_name!r}, 'item_name': {self._item_name!r}, 'wear_name': {self._wear_name!r}, 'description': {self._description!r}, 'collection': {self._collection!r}, 'serialized_inspect': {self._serialized_inspect!r}, 'gs_sig': {self._gs_sig!r}, 'high_rank': {self._high_rank!r}, 'phase': {self._phase!r}, 'sticker_index': {self._sticker_index!r}, 'badges': {self._badges!r}, 'fade': {self._fade!r}}})"

    @property
    def asset_id(self) -> str:
        """:class:`str`: Returns the asset ID of the item."""
        return self._asset_id

    @property
    def def_index(self) -> int:
        """:class:`int`: Returns the def index of the item."""
        return self._def_index

    @property
    def paint_index(self) -> Optional[int]:
        """Optional[:class:`int`]: Returns the paint index of the item."""
        return self._paint_index

    @property
    def paint_seed(self) -> Optional[int]:
        """Optional[:class:`int`]: Returns the paint seed of the item."""
        return self._paint_seed

    @property
    def float_value(self) -> Optional[float]:
        """Optional[:class:`float`]: Returns the float value of the item."""
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
    def stickers(self) -> Optional[List[Sticker]]:
        """Optional[:class:`List` of :class:`Sticker`]: Returns the attached stickers of the item."""
        return [Sticker(data=sticker) for sticker in self._stickers] if self._stickers is not None else None

    @property
    def keychains(self) -> Optional[List[Keychain]]:
        """Optional[:class:`List` of :class:`Keychain`]: Returns the attached keychains of the item."""
        return [Keychain(data=keychain) for keychain in self._keychains] if self._keychains is not None else None

    @property
    def low_rank(self) -> Optional[int]:
        """Optional[:class:`int`]: Returns the rank in FloatDB of the item."""
        return self._low_rank

    @property
    def tradable(self) -> int:
        """:class:`int`: Returns the tradable status of the item."""
        return self._tradable

    @property
    def inspect_link(self) -> str:
        """:class:`str`: Returns the inspect link of the item."""
        return self._inspect_link

    @property
    def has_screenshot(self) -> bool:
        """:class:`bool`: Returns the screenshot status of the item."""
        return self._has_screenshot

    @property
    def cs2_screenshot_id(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the CS2 screenshot ID."""
        return self._cs2_screenshot_id

    @property
    def cs2_screenshot_at(self) -> Optional[datetime.datetime]:
        """Optional[:class:`datetime.datetime`]: Returns timestamp of when the CS2 screenshot was taken."""
        return datetime.datetime.fromisoformat(self._cs2_screenshot_at) if self._cs2_screenshot_at is not None else None

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
    def wear_name(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the wear name of the item."""
        return self._wear_name

    @property
    def description(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the description of the item."""
        return self._description

    @property
    def collection(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the collection of the item."""
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
    def badges(self) -> Optional[List[str]]:
        """Optional[List[:class:`str`]]: Returns a list of badges."""
        return self._badges

    @property
    def fade(self) -> Optional[FadeInfo]:
        """Optional[:class:`FadeInfo`]: Returns the info about the fading of the item."""
        return FadeInfo(data=self._fade) if self._fade is not None else None
