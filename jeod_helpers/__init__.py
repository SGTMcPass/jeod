"""JEOD input helper utilities.

This package provides helper functions and builders to simplify
construction of Trick simulation input files.
"""

from __future__ import annotations

import logging


__all__ = [
    "__version__",
    "vehicles",
    "states",
    "gravity",
    "events",
    "builder",
]
__version__ = "0.1.0"

logger = logging.getLogger(__name__)

from . import builder, events, gravity, states, vehicles

