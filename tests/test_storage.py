import os
import json
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import storage


def test_save_and_load_snapshot(tmp_path, monkeypatch):
    test_file = tmp_path / "test_snapshots.json"
    monkeypatch.setattr(storage, "SNAPSHOTS_FILE", str(test_file))

    weather_data = {
        "city": "Baghdad",
        "temperature": 30,
        "feels_like": 29,
        "humidity": 25,
        "wind_speed": 3.5,
        "condition": "clear sky"
    }

    storage.save_snapshot(weather_data)
    snapshots = storage.load_snapshots()

    assert len(snapshots) == 1
    assert snapshots[0]["city"] == "Baghdad"
    assert snapshots[0]["temperature"] == 30


def test_load_snapshots_when_file_missing(tmp_path, monkeypatch):
    test_file = tmp_path / "does_not_exist.json"
    monkeypatch.setattr(storage, "SNAPSHOTS_FILE", str(test_file))

    snapshots = storage.load_snapshots()

    assert snapshots == []


def test_load_snapshots_when_file_corrupted(tmp_path, monkeypatch):
    test_file = tmp_path / "corrupted.json"
    test_file.write_text("this is not valid json {{{")
    monkeypatch.setattr(storage, "SNAPSHOTS_FILE", str(test_file))

    snapshots = storage.load_snapshots()

    assert snapshots == []


def test_get_snapshots_by_city(tmp_path, monkeypatch):
    test_file = tmp_path / "test_snapshots.json"
    monkeypatch.setattr(storage, "SNAPSHOTS_FILE", str(test_file))

    storage.save_snapshot({
        "city": "Baghdad", "temperature": 30, "feels_like": 29,
        "humidity": 25, "wind_speed": 3.5, "condition": "clear"
    })
    storage.save_snapshot({
        "city": "Basra", "temperature": 35, "feels_like": 34,
        "humidity": 20, "wind_speed": 2.0, "condition": "sunny"
    })

    baghdad_snapshots = storage.get_snapshots_by_city("Baghdad")

    assert len(baghdad_snapshots) == 1
    assert baghdad_snapshots[0]["city"] == "Baghdad"


def test_multiple_snapshots_accumulate(tmp_path, monkeypatch):
    test_file = tmp_path / "test_snapshots.json"
    monkeypatch.setattr(storage, "SNAPSHOTS_FILE", str(test_file))

    storage.save_snapshot({
        "city": "Baghdad", "temperature": 30, "feels_like": 29,
        "humidity": 25, "wind_speed": 3.5, "condition": "clear"
    })
    storage.save_snapshot({
        "city": "Baghdad", "temperature": 32, "feels_like": 31,
        "humidity": 22, "wind_speed": 4.0, "condition": "sunny"
    })

    snapshots = storage.load_snapshots()

    assert len(snapshots) == 2
