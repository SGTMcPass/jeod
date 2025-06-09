"""Input file builder for JEOD simulations.

This module defines a placeholder ``InputBuilder`` class that will chain helper
calls when constructing Trick input files.
"""

from __future__ import annotations

import logging
from typing import Any, List

logger = logging.getLogger(__name__)


class InputBuilder:
    """Collects actions to build a Trick input file."""

    def __init__(self) -> None:
        self.actions: List[Any] = []
        logger.debug("InputBuilder initialized")

    def add_action(self, action: Any) -> "InputBuilder":
        """Record an action for later execution."""
        logger.debug("Adding action %s", action)
        self.actions.append(action)
        return self

    def build(self) -> List[Any]:
        """Return the collected actions."""
        logger.debug("Building with %d actions", len(self.actions))
        return self.actions
