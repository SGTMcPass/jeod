# JEOD Helpers

Utility functions for building Trick input files programmatically.

## Installation

```bash
pip install -e .
```

## Basic Usage

```python
from jeod_helpers import __version__, vehicles, builder

body = vehicles.create_dyn_body("vehicle1", mass=500.0, inertia=(1, 1, 1))
from jeod_helpers import gravity
gravity.enable_spherical_gravity(body)
print(__version__, body)

from jeod_helpers import events
events.schedule_event(10.0, "trick.stop(10.0)")

# Using the InputBuilder to queue actions
bldr = builder.InputBuilder()
veh = bldr.create_body("veh", mass=500.0, inertia=(1,1,1))
bldr.set_trans_state(veh, [0,0,0], [0,0,0])
bldr.set_rot_state(veh, [0,0,0,1], [0,0,0])
actions = bldr.build()
print(actions)
```

## CLI Usage

Use the ``jeod-helpers`` command to generate a simple ``input.py``::

```bash
jeod-helpers generate my_input.py
```

The script writes a basic input file using :class:`InputBuilder`.

## Example Input File

The directory `docs/Training/Exercises/Solutions/SIM_05/SET_test/RUN_test` now contains
`input.py` rewritten using `InputBuilder`. It demonstrates how to configure a vehicle,
set its state, enable gravity, and register initialization actions programmatically.
