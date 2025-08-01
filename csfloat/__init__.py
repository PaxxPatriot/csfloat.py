"""
CSFloat API Wrapper
~~~~~~~~~~~~~~~~~~~
A basic wrapper for the CSFloat API.
:copyright: (c) 2023-present PaxxPatriot
:license: MIT, see LICENSE for more details.
"""

__title__ = "csfloat"
__author__ = "PaxxPatriot"
__license__ = "MIT"
__copyright__ = "Copyright 2023-present PaxxPatriot"
__version__ = "0.3.0"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import logging
from typing import NamedTuple

from .client import *
from .enums import *
from .errors import *
from .iterators import *
from .listing import *
from .user import *


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: int


version_info: VersionInfo = VersionInfo(major=0, minor=3, micro=0, releaselevel="final", serial=0)

logging.getLogger(__name__).addHandler(logging.NullHandler())
