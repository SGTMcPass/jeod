"""State initialization helpers for JEOD simulations."""

from __future__ import annotations

import logging
from typing import Sequence

logger = logging.getLogger(__name__)


def set_trans_state(body, position: Sequence[float], velocity: Sequence[float]):
    """Set the translational state of a body placeholder.

    Parameters
    ----------
    body : object
        Body placeholder.
    position : Sequence[float]
        Position vector [m].
    velocity : Sequence[float]
        Velocity vector [m/s].
    """
    logger.debug(
        "Setting translation for %s pos=%s vel=%s",
        getattr(body, "name", body),
        position,
        velocity,
    )
    body["position"] = list(position)
    body["velocity"] = list(velocity)


def set_rot_state(body, quaternion: Sequence[float], rates: Sequence[float]):
    """Set the rotational state of a body placeholder.

    Parameters
    ----------
    body : object
        Body placeholder.
    quaternion : Sequence[float]
        Attitude quaternion [x, y, z, w].
    rates : Sequence[float]
        Body rates [rad/s].
    """
    logger.debug(
        "Setting rotation for %s quat=%s rates=%s",
        getattr(body, "name", body),
        quaternion,
        rates,
    )
    body["quaternion"] = list(quaternion)
    body["rates"] = list(rates)
