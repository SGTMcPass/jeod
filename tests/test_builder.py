from jeod_helpers import builder


def test_builder_collect_actions(tmp_path):
    bldr = builder.InputBuilder()
    body = bldr.create_body("veh", mass=1.0, inertia=(1,1,1))
    bldr.set_trans_state(body, [0,0,0], [0,0,0])
    bldr.set_rot_state(body, [0,0,0,1], [0,0,0])
    actions = bldr.build()
    assert actions == ["veh.mass_init", "veh.trans_init", "veh.rot_init"]
