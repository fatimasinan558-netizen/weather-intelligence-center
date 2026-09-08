import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import storage
import analytics


def test_calculate_statistics_with_data(tmp_path, monkeypatch):
    test_file = tmp_path / "test_snapshots.json"
    monkeypatch.setattr(storage, "SNAPSHOTS_FILE", str(test_file))
    monkeypatch.setattr(analytics, "get_snapshots_by_city", storage.get_snapshots_by_city)

    storage.save_snapshot({"city": "Baghdad", "temperature": 30, "feels_like": 29, "humidity": 25, "wind_speed": 3.0, "condition": "clear"})
    storage.save_snapshot({"city": "Baghdad", "temperature": 40, "feels_like": 38, "humidity": 35, "wind_speed": 5.0, "condition": "sunny"})

    stats = analytics.calculate_statistics("Baghdad")

    assert stats is not None
    assert stats["temperature"]["max"] == 40
    assert stats["temperature"]["min"] == 30
    assert stats["temperature"]["average"] == 35


def test_calculate_statistics_no_data(tmp_path, monkeypatch):
    test_file = tmp_path / "empty_snapshots.json"
    monkeypatch.setattr(storage, "SNAPSHOTS_FILE", str(test_file))
    monkeypatch.setattr(analytics, "get_snapshots_by_city", storage.get_snapshots_by_city)

    stats = analytics.calculate_statistics("Basra")

    assert stats is None


def test_temperature_trend_rising(tmp_path, monkeypatch):
    test_file = tmp_path / "test_snapshots.json"
    monkeypatch.setattr(storage, "SNAPSHOTS_FILE", str(test_file))
    monkeypatch.setattr(analytics, "get_snapshots_by_city", storage.get_snapshots_by_city)

    storage.save_snapshot({"city": "Baghdad", "temperature": 25, "feels_like": 24, "humidity": 25, "wind_speed": 3.0, "condition": "clear"})
    storage.save_snapshot({"city": "Baghdad", "temperature": 35, "feels_like": 34, "humidity": 25, "wind_speed": 3.0, "condition": "clear"})

    trend = analytics.calculate_temperature_trend("Baghdad")

    assert trend == "صاعد"


def test_temperature_trend_insufficient_data(tmp_path, monkeypatch):
    test_file = tmp_path / "test_snapshots.json"
    monkeypatch.setattr(storage, "SNAPSHOTS_FILE", str(test_file))
    monkeypatch.setattr(analytics, "get_snapshots_by_city", storage.get_snapshots_by_city)

    trend = analytics.calculate_temperature_trend("Baghdad")

    assert trend == "بيانات غير كافية"
