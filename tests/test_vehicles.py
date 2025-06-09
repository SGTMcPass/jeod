import pytest
from jeod_helpers import vehicles, JeodHelperError


def test_create_dyn_body_basic():
    body = vehicles.create_dyn_body("veh")
    assert body["name"] == "veh"
    assert body["children"] == []


def test_set_mass_properties_three():
    body = {}
    vehicles.set_mass_properties(body, 1.0, (1, 2, 3))
    assert body["mass"] == 1.0
    assert body["inertia"] == [[1, 0.0, 0.0], [0.0, 2, 0.0], [0.0, 0.0, 3]]


def test_set_mass_properties_six():
    body = {}
    vehicles.set_mass_properties(body, 1.0, (1, 0.1, 0.2, 2, 0.3, 3))
    assert body["mass"] == 1.0
    assert body["inertia"] == [[1, 0.1, 0.2], [0.1, 2, 0.3], [0.2, 0.3, 3]]


def test_set_mass_properties_nine():
    body = {}
    vehicles.set_mass_properties(body, 1.0, (1,2,3,4,5,6,7,8,9))
    assert body["mass"] == 1.0
    assert body["inertia"] == [[1,2,3],[4,5,6],[7,8,9]]


def test_attach_body():
    parent = {"name": "p"}
    child = {"name": "c"}
    vehicles.attach_body(parent, child)
    assert child in parent["children"]


def test_set_mass_properties_invalid():
    body = {}
    with pytest.raises(JeodHelperError):
        vehicles.set_mass_properties(body, -1, (1,2,3))
    with pytest.raises(JeodHelperError):
        vehicles.set_mass_properties(body, 1, (1,2))
