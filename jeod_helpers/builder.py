"""Input file builder for JEOD simulations.

This module provides :class:`InputBuilder`, a convenience class that chains the
helper functions defined in this package and records body initialization actions
to mimic calls to ``dynamics.dyn_manager.add_body_action``.  Each method returns
``self`` so builders can be used in a fluent style.  The collected actions are
stored in the order added and can be retrieved with :meth:`build`.
"""

from __future__ import annotations

import logging
from typing import Any, List

from . import states, vehicles

logger = logging.getLogger(__name__)


class InputBuilder:
    """Collect body initialization actions for a Trick simulation."""

    def __init__(self) -> None:
        self.bodies: List[Any] = []
        self.body_actions: List[Any] = []
        logger.debug("InputBuilder initialized")

    # ------------------------------------------------------------------
    # Body creation helpers
    # ------------------------------------------------------------------
    def create_body(self, name: str, *, mass: float | None = None, inertia: List[float] | None = None) -> Any:
        """Create a body placeholder and record any mass init action."""
        body = vehicles.create_dyn_body(name, mass=mass, inertia=inertia)
        self.bodies.append(body)
        logger.info("Created body %s", name)
        if mass is not None and inertia is not None:
            self.body_actions.append(f"{name}.mass_init")
        return body

    def attach(self, parent: Any, child: Any) -> "InputBuilder":
        """Attach ``child`` to ``parent`` in the dynamics tree."""
        vehicles.attach_body(parent, child)
        logger.info("Queued attach %s -> %s", child.get("name"), parent.get("name"))
        return self

    # ------------------------------------------------------------------
    # State setup helpers
    # ------------------------------------------------------------------
    def set_trans_state(self, body: Any, position: List[float], velocity: List[float], **kwargs) -> "InputBuilder":
        states.set_trans_state(body, position, velocity, **kwargs)
        self.body_actions.append(f"{body.get('name')}.trans_init")
        logger.info("Queued trans_init for %s", body.get("name"))
        return self

    def set_rot_state(self, body: Any, quaternion: List[float], rates: List[float], **kwargs) -> "InputBuilder":
        states.set_rot_state(body, quaternion, rates, **kwargs)
        self.body_actions.append(f"{body.get('name')}.rot_init")
        logger.info("Queued rot_init for %s", body.get("name"))
        return self

    def set_mass_properties(self, body: Any, mass: float, inertia: List[float]) -> "InputBuilder":
        vehicles.set_mass_properties(body, mass, inertia)
        self.body_actions.append(f"{body.get('name')}.mass_init")
        logger.info("Queued mass_init for %s", body.get("name"))
        return self

    # ------------------------------------------------------------------
    def build(self) -> List[Any]:
        """Return the ordered list of body actions."""
        logger.debug("Building with %d body actions", len(self.body_actions))
        return self.body_actions
