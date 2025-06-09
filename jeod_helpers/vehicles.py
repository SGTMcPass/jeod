"""Vehicle creation helpers for JEOD simulations.

This module will provide utility functions for building and configuring
`DynBody` objects used within Trick input files.
"""

from __future__ import annotations

import logging
from typing import Sequence

logger = logging.getLogger(__name__)


def create_dyn_body(name: str):
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
    logger.debug("Creating DynBody: %s", name)
    # Placeholder return until Trick environment available
    return {"name": name}


def set_mass_properties(body, mass: float, inertia):
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
    logger.debug(
        "Setting mass properties for %s: mass=%s inertia=%s",
        getattr(body, "name", body),
        mass,
        inertia,
    )
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
    elif len(inertia) == 9:
        inertia_matrix = [
            list(inertia[0:3]),
            list(inertia[3:6]),
            list(inertia[6:9]),
        ]
    else:
        raise ValueError("Inertia must have 3, 6, or 9 elements")

    body["inertia"] = inertia_matrix


def attach_body(parent, child):
    """Attach one body to another in the dynamics tree.

    Parameters
    ----------
    parent : object
        Parent body.
    child : object
        Child body to attach.
    """
    logger.debug("Attaching %s to %s", getattr(child, "name", child), getattr(parent, "name", parent))
    # Placeholder logic for attachment
    parent.setdefault("children", []).append(child)
