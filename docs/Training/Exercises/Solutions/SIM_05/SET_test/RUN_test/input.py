# Rewritten example using jeod_helpers InputBuilder

from jeod_helpers import builder, gravity
from jeod_helpers import events

# ---------------------------------------------
# Set up Trick executive parameters.
# ---------------------------------------------
# trick.sim_services.exec_set_trap_sigfpe(1)

# Set up data recording
exec(compile(open("Log_data/log_state.py", "rb").read(), "Log_data/log_state.py", 'exec'))
log_state(1.0)

# Configure the dynamics manager to operate in empty space mode

dynamics.dyn_manager_init.mode = trick.DynManagerInit.EphemerisMode_EmptySpace
dynamics.dyn_manager_init.central_point_name = "Space"

rk_integrator = trick.RK4IntegratorConstructor()
dynamics.dyn_manager_init.integ_constructor = rk_integrator

# Create vehicle body using the InputBuilder
bldr = builder.InputBuilder()
vehicle = bldr.create_body("veh", mass=500.0, inertia=(1, 0, 0, 0, 1, 0, 0, 0, 1))

# Set translational and rotational states
bldr.set_trans_state(vehicle, [10, 0, 0], [-2, 0, 0])
bldr.set_rot_state(vehicle, [0, 0, 1, 0], [0, 0, -36], rate_units="degree/s")

# Enable spherical gravity
gravity.enable_spherical_gravity(vehicle)

# Register initialization actions with the dynamics manager
for action in bldr.build():
    # action names like "veh.mass_init" -- use eval to get the actual object
    dynamics.dyn_manager.add_body_action(eval(action))

trick.sim_services.exec_set_terminate_time(10.0)

