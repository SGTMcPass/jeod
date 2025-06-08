"""Gravity configuration helpers."""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


def enable_spherical_gravity(body, planet: str = "earth"):
    """Enable simple spherical gravity for a body placeholder."""
    logger.debug("Enabling spherical gravity for %s around %s", getattr(body, "name", body), planet)
    body.setdefault("gravity", {})["type"] = "spherical"
    body["gravity"]["planet"] = planet


def enable_spherical_harmonics(body, degree: int, order: int, planet: str = "earth"):
    """Enable spherical harmonics gravity."""
    logger.debug(
        "Enabling harmonics for %s deg=%s order=%s planet=%s",
        getattr(body, "name", body),
        degree,
        order,
        planet,
    )
    body.setdefault("gravity", {})["type"] = "harmonics"
    body["gravity"].update({"degree": degree, "order": order, "planet": planet})
