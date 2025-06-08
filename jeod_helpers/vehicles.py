"""Vehicle creation helpers for JEOD simulations.

This module will provide utility functions for building and configuring
`DynBody` objects used within Trick input files.
"""

from __future__ import annotations

import logging

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


def set_mass_properties(body, mass: float, inertia: tuple[float, float, float]):
    """Assign mass properties to a DynBody placeholder.

    Parameters
    ----------
    body : object
        The body object to modify.
    mass : float
        Mass value in kilograms.
    inertia : tuple[float, float, float]
        Principal moments of inertia in kg-m^2.
    """
    logger.debug(
        "Setting mass properties for %s: mass=%s inertia=%s",
        getattr(body, "name", body),
        mass,
        inertia,
    )
    body["mass"] = mass
    body["inertia"] = inertia


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
