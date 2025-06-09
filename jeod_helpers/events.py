"""Event scheduling helpers.

This module wraps common Trick logging and event scheduling calls to
make them traceable when the Trick environment is available. All
functions log with a timestamp so generated input files can be audited.
"""

from __future__ import annotations

import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def add_data_record_group(dr_group):
    """Add a Trick data recording group with timestamped logging.

    Parameters
    ----------
    dr_group : object
        Typically an instance of ``trick.sim_services.DRBinary``.
    """
    timestamp = datetime.now().isoformat()
    name = getattr(dr_group, "name", dr_group)
    logger.info("[%s] add_data_record_group %s", timestamp, name)
    try:  # pragma: no cover - Trick not installed in CI
        import trick

        trick.add_data_record_group(dr_group)
    except Exception:
        logger.debug("trick.add_data_record_group not available")
    return dr_group


def schedule_event(time: float, action: str):
    """Schedule an action at the specified simulation time.

    Parameters
    ----------
    time : float
        Simulation time of the event.
    action : str
        Trick command string to execute.
    """
    timestamp = datetime.now().isoformat()
    logger.info("[%s] schedule_event t=%s action=%s", timestamp, time, action)
    try:  # pragma: no cover - Trick not installed in CI
        import trick

        event = trick.new_event(f"evt_{time}")
        event.condition(0, f"trick.exec_get_sim_time() >= {time}")
        event.condition_all()
        event.set_cycle(time)
        event.action(0, action)
        event.activate()
        trick.add_event(event)
        return event
    except Exception:
        logger.debug("trick.add_event fallback")
        return {"time": time, "action": action}
