"""State initialization helpers for JEOD simulations."""

from __future__ import annotations

import logging
from typing import Sequence

from . import JeodHelperError

logger = logging.getLogger(__name__)


def _attach_units(units: str, value: Sequence[float]):
    """Return a value with Trick units attached if available."""
    try:
        from trick import sim_services

        return sim_services.attach_units(units, value)
    except Exception:  # pragma: no cover - Trick not installed
        logger.debug("attach_units fallback for %s", units)
        return list(value)


def set_trans_state(
    body,
    position: Sequence[float],
    velocity: Sequence[float],
    *,
    pos_units: str = "m",
    vel_units: str = "m/s",
):
    """Set the translational state of a body placeholder.

    Parameters
    ----------
    body : object
        Body placeholder.
    position : Sequence[float]
        Position vector.
    velocity : Sequence[float]
        Velocity vector.
    pos_units : str, optional
        Units for the position vector, by default "m".
    vel_units : str, optional
        Units for the velocity vector, by default "m/s".
    """
    if len(position) != 3 or len(velocity) != 3:
        logger.warning("Bad state vector lengths pos=%s vel=%s", position, velocity)
        raise JeodHelperError("Position and velocity must be 3-element sequences")

    logger.info(
        "Setting translation for %s pos=%s %s vel=%s %s",
        getattr(body, "name", body),
        position,
        pos_units,
        velocity,
        vel_units,
    )
    body["position"] = _attach_units(pos_units, position)
    body["velocity"] = _attach_units(vel_units, velocity)


def set_rot_state(
    body,
    quaternion: Sequence[float],
    rates: Sequence[float],
    *,
    quat_units: str = "dimensionless",
    rate_units: str = "rad/s",
):
    """Set the rotational state of a body placeholder.

    Parameters
    ----------
    body : object
        Body placeholder.
    quaternion : Sequence[float]
        Attitude quaternion ``[x, y, z, w]``.
    rates : Sequence[float]
        Body rates.
    quat_units : str, optional
        Units for the quaternion, usually dimensionless.
    rate_units : str, optional
        Units for the angular velocity, by default ``"rad/s"``.
    """
    if len(quaternion) != 4 or len(rates) != 3:
        logger.warning("Bad rotation vector lengths quat=%s rates=%s", quaternion, rates)
        raise JeodHelperError("Quaternion must have 4 elements and rates 3")

    logger.info(
        "Setting rotation for %s quat=%s %s rates=%s %s",
        getattr(body, "name", body),
        quaternion,
        quat_units,
        rates,
        rate_units,
    )
    body["quaternion"] = _attach_units(quat_units, quaternion)
    body["rates"] = _attach_units(rate_units, rates)

    return body
