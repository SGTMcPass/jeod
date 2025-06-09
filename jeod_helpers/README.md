# JEOD Helpers

Utility functions for building Trick input files programmatically.

## Installation

```bash
pip install -e .
```

## Basic Usage

```python
from jeod_helpers import __version__, vehicles

body = vehicles.create_dyn_body("vehicle1", mass=500.0, inertia=(1, 1, 1))
from jeod_helpers import gravity
gravity.enable_spherical_gravity(body)
print(__version__, body)

from jeod_helpers import events
events.schedule_event(10.0, "trick.stop(10.0)")
```
