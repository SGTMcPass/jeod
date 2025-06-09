import pytest
from jeod_helpers import gravity, JeodHelperError


def test_configure_gravity_spherical():
    body = {"name": "veh"}
    gravity.configure_gravity_controls(body)
    assert body["gravity"] == {"type": "spherical", "planet": "earth"}


def test_configure_gravity_harmonics():
    body = {"name": "veh"}
    gravity.configure_gravity_controls(body, use_harmonics=True, degree=2, order=2, planet="mars")
    assert body["gravity"] == {"type": "harmonics", "degree": 2, "order": 2, "planet": "mars"}


def test_configure_gravity_bad():
    body = {}
    with pytest.raises(JeodHelperError):
        gravity.configure_gravity_controls(body, use_harmonics=True)
