import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import rules


def test_check_thresholds_hot_temperature():
    weather_data = {"temperature": 45, "humidity": 30, "wind_speed": 2}
    alerts = rules.check_thresholds(weather_data)
    assert any("الحرارة عالية" in a for a in alerts)


def test_check_thresholds_no_alerts():
    weather_data = {"temperature": 25, "humidity": 45, "wind_speed": 3}
    alerts = rules.check_thresholds(weather_data)
    assert alerts == []


def test_decision_table_no_alerts():
    result = rules.decision_table([])
    assert result == "لا توجد تنبيهات"


def test_decision_table_multiple_alerts():
    result = rules.decision_table(["تنبيه1", "تنبيه2", "تنبيه3"])
    assert "خطرة" in result


def test_calculate_comfort_score_perfect_weather():
    weather_data = {"temperature": 22, "humidity": 45, "wind_speed": 2}
    result = rules.calculate_comfort_score(weather_data)
    assert result["score"] == 100
    assert "مريح" in result["explanation"]


def test_calculate_comfort_score_extreme_heat():
    weather_data = {"temperature": 45, "humidity": 30, "wind_speed": 2}
    result = rules.calculate_comfort_score(weather_data)
    assert result["score"] < 100
    assert "الحرارة" in result["explanation"]
