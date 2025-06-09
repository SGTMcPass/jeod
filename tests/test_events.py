from jeod_helpers import events


def test_add_data_record_group():
    obj = type("DR", (), {"name": "grp"})()
    result = events.add_data_record_group(obj)
    assert result == obj


def test_schedule_event():
    event = events.schedule_event(1.0, "do_something")
    assert event["time"] == 1.0
    assert event["action"] == "do_something"
