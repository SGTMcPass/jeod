"""Event scheduling helpers."""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


def schedule_event(time: float, action: str):
    """Schedule a simple string action at simulation time."""
    logger.debug("Scheduling event %s at t=%s", action, time)
    return {"time": time, "action": action}
