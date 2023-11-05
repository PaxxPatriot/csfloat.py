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
from typing import Any, Callable, Coroutine, Dict, List, Optional, Union

from .errors import BadRequest
from .listing import Listing


class ListingAsyncIterator:
    def __init__(
        self,
        getter: Callable[..., Coroutine[Any, Any, Any]],
        limit: Optional[int] = None,
        pagination_token: int = 0,
        **kwargs: Dict[str, Any],
    ) -> None:
        self.limit = limit
        self.has_more = True
        self.getter = getter
        self.kwargs = kwargs

        self.listings: asyncio.Queue[Listing] = asyncio.Queue()
        self.pagination_token = pagination_token
        self.next_token = pagination_token + 1

    async def __anext__(self):
        try:
            return await self.next()
        except StopAsyncIteration as e:
            raise

    def __aiter__(self):
        return self

    async def flatten(self):
        return [element async for element in self]

    async def next(self) -> Listing:
        if self.listings.empty():
            await self.fill_listings()

        try:
            return self.listings.get_nowait()
        except asyncio.QueueEmpty as e:
            raise StopAsyncIteration from e

    async def fill_listings(self):
        if not self.has_more:
            raise StopAsyncIteration

        self.kwargs["page"] = self.pagination_token
        try:
            listings: List[Dict[str, Any]] = await self.getter(params=self.kwargs)
        except BadRequest:
            self.has_more = False
            return

        for l in reversed(listings):
            self.listings.put_nowait(Listing(data=l))

        self.pagination_token = self.next_token
        self.next_token = self.pagination_token + 1
