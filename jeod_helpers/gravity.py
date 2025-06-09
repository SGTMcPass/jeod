"""Gravity configuration helpers."""

from __future__ import annotations

import logging

from . import JeodHelperError

logger = logging.getLogger(__name__)


def enable_spherical_gravity(body, planet: str = "earth"):
    """Enable simple spherical gravity for a body placeholder."""
    logger.info(
        "Enabling spherical gravity for %s around %s",
        getattr(body, "name", body),
        planet,
    )
    body.setdefault("gravity", {})["type"] = "spherical"
    body["gravity"]["planet"] = planet


def enable_spherical_harmonics(
    body, degree: int, order: int, planet: str = "earth"
):
    """Enable spherical harmonics gravity."""
    logger.info(
        "Enabling harmonics for %s deg=%s order=%s planet=%s",
        getattr(body, "name", body),
        degree,
        order,
        planet,
    )
    if degree <= 0 or order <= 0:
        raise JeodHelperError("degree and order must be positive")

    body.setdefault("gravity", {})["type"] = "harmonics"
    body["gravity"].update({"degree": degree, "order": order, "planet": planet})


def configure_gravity_controls(
    body,
    *,
    use_harmonics: bool = False,
    degree: int | None = None,
    order: int | None = None,
    planet: str = "earth",
):
    """General gravity control wrapper with fail-soft validation."""
    if use_harmonics:
        if degree is None or order is None:
            raise JeodHelperError("degree and order required for harmonics")
        enable_spherical_harmonics(body, degree, order, planet)
    else:
        enable_spherical_gravity(body, planet)
    return body
