import pytest
from jeod_helpers import states, JeodHelperError


def test_set_trans_state_ok():
    body = {"name": "veh"}
    states.set_trans_state(body, [1,2,3], [4,5,6])
    assert body["position"] == [1,2,3]
    assert body["velocity"] == [4,5,6]


def test_set_trans_state_bad():
    body = {}
    with pytest.raises(JeodHelperError):
        states.set_trans_state(body, [1,2], [3,4,5])


def test_set_rot_state_ok():
    body = {"name": "veh"}
    states.set_rot_state(body, [0,0,0,1], [0,0,0])
    assert body["quaternion"] == [0,0,0,1]
    assert body["rates"] == [0,0,0]


def test_set_rot_state_bad():
    body = {}
    with pytest.raises(JeodHelperError):
        states.set_rot_state(body, [0,0,0], [0,0])
