"""Vehicle creation helpers for JEOD simulations.

This module will provide utility functions for building and configuring
`DynBody` objects used within Trick input files.
"""

from __future__ import annotations

import logging
from typing import Sequence

from . import JeodHelperError

logger = logging.getLogger(__name__)


def create_dyn_body(name: str, *, mass: float | None = None, inertia: Sequence[float] | None = None):
    """Create a bare DynBody placeholder.

    Parameters
    ----------
    name : str
        The name of the body to create.

    Returns
    -------
    object
        Placeholder for a Trick DynBody instance.
    """
    logger.info("Creating DynBody: %s", name)
    body = {"name": name, "children": []}
    if mass is not None and inertia is not None:
        set_mass_properties(body, mass, inertia)
    elif mass is not None or inertia is not None:
        logger.warning("Both mass and inertia required to set properties; ignoring")
    return body


def set_mass_properties(body, mass: float, inertia: Sequence[float]):
    """Assign mass properties to a DynBody placeholder.

    Parameters
    ----------
    body : object
        The body object to modify.
    mass : float
        Mass value in kilograms.
    inertia : Sequence[float]
        Moments of inertia. Accepts 3 values ``(Ixx, Iyy, Izz)`` for a
        diagonal inertia tensor, 6 values ``(Ixx, Ixy, Ixz, Iyy, Iyz, Izz)``
        for a symmetric tensor, or 9 values providing the full 3x3 matrix
        in row-major order.
    """
    logger.info(
        "Setting mass properties for %s",
        getattr(body, "name", body),
    )
    if mass <= 0:
        raise JeodHelperError("Mass must be positive")
    if len(inertia) not in (3, 6, 9):
        raise JeodHelperError("Inertia must have 3, 6, or 9 elements")

    body["mass"] = mass
    if len(inertia) == 3:
        Ixx, Iyy, Izz = inertia
        inertia_matrix = [
            [Ixx, 0.0, 0.0],
            [0.0, Iyy, 0.0],
            [0.0, 0.0, Izz],
        ]
    elif len(inertia) == 6:
        Ixx, Ixy, Ixz, Iyy, Iyz, Izz = inertia
        inertia_matrix = [
            [Ixx, Ixy, Ixz],
            [Ixy, Iyy, Iyz],
            [Ixz, Iyz, Izz],
        ]
    else:
        inertia_matrix = [
            list(inertia[0:3]),
            list(inertia[3:6]),
            list(inertia[6:9]),
        ]

    body["inertia"] = inertia_matrix
    logger.debug("Inertia matrix for %s: %s", getattr(body, "name", body), inertia_matrix)


def attach_body(parent, child):
    """Attach one body to another in the dynamics tree.

    Parameters
    ----------
    parent : object
        Parent body.
    child : object
        Child body to attach.
    """
    logger.info(
        "Attaching %s to %s",
        getattr(child, "name", child),
        getattr(parent, "name", parent),
    )
    parent.setdefault("children", []).append(child)
    logger.debug("%s now has %d children", getattr(parent, "name", parent), len(parent["children"]))
