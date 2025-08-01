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

__all__ = (
    "FirebaseMessaging",
    "PaymentAccounts",
    "UserStatistics",
    "AuthenticatedUserStatistics",
    "UserPreferences",
    "User",
    "AuthenticatedUser",
)

import datetime
from typing import Any, Dict, List, Optional


class FirebaseMessaging:
    __slots__ = (
        "_platform",
        "_last_updated",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._platform = data.get("platform", None)
        self._last_updated = data.get("last_updated", None)

    def __repr__(self) -> str:
        return f"FirebaseMessaging(data={{'platform': {self._platform!r}, 'last_updated': {self._last_updated!r}}})"

    @property
    def platform(self) -> Optional[str]:
        return self._platform

    @property
    def last_update(self) -> Optional[datetime.datetime]:
        return datetime.datetime.fromisoformat(self._last_updated) if self._last_updated is not None else None


class PaymentAccounts:
    __slots__ = (
        "_stripe_connect",
        "_stripe_customer",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._stripe_connect = data.get("stripe_connect", "")
        self._stripe_customer = data.get("stripe_customer", "")

    def __repr__(self) -> str:
        return f"PaymentAccounts(data={{'stripe_connect': {self._stripe_connect!r}, 'stripe_customer': {self._stripe_customer!r}}})"

    @property
    def stripe_connect(self) -> str:
        """:class:`str`: Returns Stripe account ID."""
        return self._stripe_connect

    @property
    def stripe_customer(self) -> str:
        """:class:`str`: Returns Stripe customer ID."""
        return self._stripe_customer


class UserStatistics:
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

    def __repr__(self) -> str:
        return f"UserStatistics(data={{'median_trade_time': {self._median_trade_time!r}, 'total_avoided_trades': {self._total_avoided_trades!r}, 'total_failed_trades': {self._total_failed_trades!r}, 'total_trades': {self._total_trades!r}, 'total_verified_trades': {self._total_verified_trades!r}}})"

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


class AuthenticatedUserStatistics(UserStatistics):
    __slots__ = (
        "_total_sales",
        "_total_purchases",
    )

    def __init__(self, data: Dict[str, Any]) -> None:
        super().__init__(data=data)
        self._total_sales = data.get("total_sales", 0)
        self._total_purchases = data.get("total_purchases", 0)

    def __repr__(self) -> str:
        return f"AuthenticatedUserStatistics(data={{'median_trade_time': {self._median_trade_time!r}, 'total_avoided_trades': {self._total_avoided_trades!r}, 'total_failed_trades': {self._total_failed_trades!r}, 'total_trades': {self._total_trades!r}, 'total_verified_trades': {self._total_verified_trades!r}, 'total_sales': {self._total_sales!r}, 'total_purchases': {self._total_purchases!r}}})"

    @property
    def total_sales(self) -> float:
        """:class:`float`: Returns the figure of total sales in USD."""
        return self._total_sales / 100

    @property
    def total_purchases(self) -> float:
        """:class:`float`: Returns the figure of total purchases in USD."""
        return self._total_purchases / 100


class UserPreferences:
    __slots__ = (
        "_offers_enabled",
        "_max_offer_discount",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._offers_enabled = data.get("offers_enabled", True)
        self._max_offer_discount = data.get("max_offer_discount", 0)

    def __repr__(self) -> str:
        return f"UserPreferences(data={{'offers_enabled': {self._offers_enabled!r}, 'max_offer_discount': {self._max_offer_discount!r}}})"

    @property
    def offers_enabled(self) -> bool:
        """:class:`bool`: Returns if bargaining is enabled."""
        return self._offers_enabled

    @property
    def max_offer_discount(self) -> float:
        """:class:`float`: Returns the maximum discount in percent which is set when bargaining is enabled."""
        return self._max_offer_discount / 100


class User:
    __slots__ = (
        "_avatar",
        "_away",
        "_flags",
        "_obfuscated_id",
        "_has_valid_steam_api_key",
        "_online",
        "_stall_public",
        "_statistics",
        "_steam_id",
        "_username",
        "_verification_mode",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._avatar = data.get("avatar", None)
        self._away = data.get("away", False)
        self._flags = data.get("flags")
        self._obfuscated_id = data.get("obfuscated_id", None)
        self._has_valid_steam_api_key = data.get("has_valid_steam_api_key", False)
        self._online = data.get("online", False)
        self._stall_public = data.get("stall_public", False)
        self._statistics = data.get("statistics")
        self._steam_id = data.get("steam_id", None)
        self._username = data.get("username", None)
        self._verification_mode = data.get("verification_mode", None)

    def __repr__(self) -> str:
        return f"User(data={{'avatar': {self._avatar!r}, 'away': {self._away!r}, 'flags': {self._flags!r}, 'obfuscated_id': {self._obfuscated_id!r}, 'has_valid_steam_api_key': {self._has_valid_steam_api_key!r}, 'online': {self._online!r}, 'stall_public': {self._stall_public!r}, 'statistics': {self._statistics!r}, 'steam_id': {self._steam_id!r}, 'username': {self._username!r}, 'verification_mode': {self._verification_mode!r}}})"

    @property
    def avatar(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the URL to the avatar of the seller."""
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
    def obfuscated_id(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the obfuscated ID of the seller."""
        return self._obfuscated_id

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
    def statistics(self) -> UserStatistics:
        """:class:`Any`: Returns the statistics of the seller."""
        return UserStatistics(data=self._statistics)

    @property
    def steam_id(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the Steam ID of the seller."""
        return self._steam_id

    @property
    def username(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the username of the seller."""
        return self._username

    @property
    def verification_mode(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the verification mode of the seller."""
        return self._verification_mode


class AuthenticatedUser(User):
    __slots__ = (
        "_background_url",
        "_email",
        "_balance",
        "_pending_balance",
        "_trade_token",
        "_payment_accounts",
        "_api_key",
        "_statistics",
        "_preferences",
        "_know_your_customer",
        "_obfuscated_id",
        "_fee",
        "_withdraw_fee",
        "_subscriptions",
        "_has_2fa",
        "_extension_setup_at",
        "_firebase_messaging",
        "_stripe_connect",
        "_has_api_key",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        super().__init__(data=data)
        self._background_url = data.get("background_url", "")
        self._email = data.get("email", "")
        self._balance = data.get("balance", 0)
        self._pending_balance = data.get("pending_balance", 0)
        self._trade_token = data.get("trade_token", "")
        self._payment_accounts = data.get("payment_accounts", None)
        self._api_key = data.get("api_key")
        self._statistics = data.get("statistics", None)
        self._preferences = data.get("preferences", None)
        self._know_your_customer = data.get("know_your_customer", "")
        self._obfuscated_id = data.get("obfuscated_id", "")
        self._fee = data.get("fee", 0.0)
        self._withdraw_fee = data.get("withdraw_fee", 0.0)
        self._subscriptions = data.get("subscriptions", [])
        self._has_2fa = data.get("has_2fa", False)
        self._extension_setup_at = data.get("extension_setup_at", "1970-01-01T00:00:00.000000Z")
        self._firebase_messaging = data.get("firebase_messaging")
        self._stripe_connect = data.get("stripe_connect")
        self._has_api_key = data.get("has_api_key", False)

    def __repr__(self) -> str:
        return f"AuthenticatedUser(data={{'avatar': {self._avatar!r}, 'away': {self._away!r}, 'flags': {self._flags!r}, 'obfuscated_id': {self._obfuscated_id!r}, 'has_valid_steam_api_key': {self._has_valid_steam_api_key!r}, 'online': {self._online!r}, 'stall_public': {self._stall_public!r}, 'statistics': {self._statistics!r}, 'steam_id': {self._steam_id!r}, 'username': {self._username!r}, 'verification_mode': {self._verification_mode!r}, 'background_url': {self._background_url!r}, 'email': {self._email!r}, 'balance': {self._balance!r}, 'pending_balance': {self._pending_balance!r}, 'trade_token': {self._trade_token!r}, 'payment_accounts': {self._payment_accounts!r}, 'api_key': {self._api_key!r}, 'preferences': {self._preferences!r}, 'know_your_customer': {self._know_your_customer!r}, 'fee': {self._fee!r}, 'withdraw_fee': {self._withdraw_fee!r}, 'subscriptions': {self._subscriptions!r}, 'has_2fa': {self._has_2fa!r}, 'extension_setup_at': {self._extension_setup_at!r}, 'firebase_messaging': {self._firebase_messaging!r}, 'stripe_connect': {self._stripe_connect!r}, 'has_api_key': {self._has_api_key!r}}})"

    @property
    def background_url(self) -> str:
        """:class:`Any`: Returns the background URL of the user."""
        return self._background_url

    @property
    def email(self) -> str:
        """:class:`Any`: Returns the email of the user."""
        return self._email

    @property
    def balance(self) -> float:
        """:class:`Any`: Returns the balance of the user."""
        return self._balance / 100

    @property
    def pending_balance(self) -> float:
        """:class:`Any`: Returns the pending balance of the user."""
        return self._pending_balance / 100

    @property
    def trade_token(self) -> str:
        """:class:`Any`: Returns the trade token of the user."""
        return self._trade_token

    @property
    def payment_accounts(self) -> PaymentAccounts:
        """:class:`Any`: Returns the payment accounts of the user."""
        return PaymentAccounts(data=self._payment_accounts)

    @property
    def api_key(self) -> Optional[str]:
        """Optional[:class:`str`]: Returns the API key of the user."""
        return self._api_key

    @property
    def statistics(self) -> AuthenticatedUserStatistics:
        """:class:`AuthenticatedUserStatistics`: Returns the statistics of the user."""
        return AuthenticatedUserStatistics(data=self._statistics)

    @property
    def preferences(self) -> UserPreferences:
        """:class:`UserPreferences`: Returns the preferences of the user."""
        return UserPreferences(data=self._preferences)

    @property
    def know_your_customer(self) -> str:
        """:class:`Any`: Returns the know your customer information of the user."""
        return self._know_your_customer

    @property
    def obfuscated_id(self) -> str:
        """:class:`Any`: Returns the obfuscated ID of the user."""
        return self._obfuscated_id

    @property
    def fee(self) -> float:
        """:class:`Any`: Returns the fee of the user."""
        return self._fee

    @property
    def withdraw_fee(self) -> float:
        """:class:`Any`: Returns the withdraw fee of the user."""
        return self._withdraw_fee

    @property
    def subscriptions(self) -> List[str]:
        """:class:`Any`: Returns the subscriptions of the user."""
        return self._subscriptions

    @property
    def has_2fa(self) -> bool:
        """:class:`Any`: Returns the 2FA status of the user."""
        return self._has_2fa

    @property
    def extension_setup_at(self) -> datetime.datetime:
        """:class:`datetime.datetime`: Returns the date and time when the CSFloat extension was set up."""
        return datetime.datetime.fromisoformat(self._extension_setup_at)

    @property
    def firebase_messaging(self) -> FirebaseMessaging:
        return FirebaseMessaging(data=self._firebase_messaging)

    @property
    def stripe_connect(self) -> Dict[str, bool]:
        return self._stripe_connect

    @property
    def has_api_key(self) -> bool:
        return self._has_api_key
