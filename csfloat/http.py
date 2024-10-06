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
import sys
import time
from typing import Any, Dict, Iterable, List, Optional

import aiohttp

from csfloat import __version__

from .errors import BadRequest, Forbidden, HTTPException, InternalServerError, NotFound, Unauthorized

_log = logging.getLogger(__name__)


class Route:
    BASE = "https://csfloat.com/api/v1"

    def __init__(self, method: str, path: str) -> None:
        self.path: str = path
        self.method: str = method
        self.url: str = self.BASE + self.path


class HTTPClient:
    def __init__(
        self,
        *,
        proxy: Optional[str] = None,
        proxy_auth: Optional[aiohttp.BasicAuth] = None,
    ) -> None:
        self.__session = aiohttp.ClientSession()
        self.api_key = None
        self.proxy: Optional[str] = proxy
        self.proxy_auth: Optional[aiohttp.BasicAuth] = proxy_auth

        user_agent = "csfloat.py {0}) Python/{1[0]}.{1[1]} aiohttp/{2}"
        self.user_agent: str = user_agent.format(__version__, sys.version_info, str(aiohttp.__version__))

    def set_api_key(self, api_key: str) -> None:
        self.api_key = api_key

    async def close(self) -> None:
        if self.__session:
            await self.__session.close()

    async def request(
        self,
        route: Route,
        params: Optional[Iterable[Dict[str, Any]]] = None,
        **kwargs: Any,
    ) -> Any:
        method = route.method
        url = route.url

        # header creation
        headers: Dict[str, str] = {
            "User-Agent": self.user_agent,
        }

        if self.api_key is not None:
            headers["Authorization"] = self.api_key

        kwargs["headers"] = headers

        if params:
            kwargs["params"] = params

        async with self.__session.request(method, url, **kwargs) as response:
            for _ in range(2):
                _log.info(f"{method} {url} with {kwargs} has returned {response.status}")

                data = await response.json()

                if 300 > response.status >= 200:
                    _log.debug(f"{method} {url} has received {data}")
                    return data

                if response.status in {500, 503}:
                    raise InternalServerError(response, data)

                if response.status == 400:
                    raise BadRequest(response, data)
                if response.status == 401:
                    raise Unauthorized(response, data)
                if response.status == 403:
                    raise Forbidden(response, data)
                if response.status == 404:
                    raise NotFound(response, data)
                if response.status == 429:
                    # We are getting rate-limited, read x-ratelimit-reset header and calculate cooldown
                    default_ratelimit_time = int(time.time()) + 600
                    ratelimit_reset = int(headers.get("X-Ratelimit-Reset", default_ratelimit_time))
                    wait_time = ratelimit_reset - int(time.time())
                    _log.info(f"{method} {url} is getting rate-limited, retry after {wait_time} seconds")
                    await asyncio.sleep(wait_time)
                    continue
                raise HTTPException(response, data)

    async def get_all_listings(self, **parameters: Any) -> List[Dict[str, Any]]:
        return await self.request(Route("GET", "/listings"), **parameters)

    async def get_listing(self, item_id: int) -> Dict[str, Any]:
        return await self.request(Route("GET", f"/listings/{item_id}"))

    async def list_item(self, parameters: Dict) -> List[Dict[str, Any]]:
        return await self.request(Route("POST", "/listings"), json=parameters)

    # Undocumented endpoints (only usable with an API key)
    async def me(self) -> Dict[str, Any]:
        return await self.request(Route("GET", "/me"))

    async def get_inventory(self) -> List[Dict[str, Any]]:
        return await self.request(Route("GET", "/me/inventory"))

    async def unlist_item(self, listing_id: int) -> Dict[str, str]:
        return await self.request(Route("DELETE", f"/listings/{listing_id}"))
