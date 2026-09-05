import os
import sys
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import api_weather


def test_fetch_weather_success():
    fake_response = MagicMock()
    fake_response.status_code = 200
    fake_response.json.return_value = {
        "name": "Baghdad",
        "main": {"temp": 30, "feels_like": 29, "humidity": 25},
        "wind": {"speed": 3.5},
        "weather": [{"description": "clear sky"}]
    }

    with patch("api_weather.requests.get", return_value=fake_response):
        result = api_weather.fetch_weather("Baghdad")

    assert result is not None
    assert result["city"] == "Baghdad"
    assert result["temperature"] == 30
    assert result["humidity"] == 25


def test_fetch_weather_city_not_found():
    fake_response = MagicMock()
    fake_response.status_code = 404

    with patch("api_weather.requests.get", return_value=fake_response):
        result = api_weather.fetch_weather("CityThatDoesNotExist")

    assert result is None


def test_fetch_weather_timeout():
    with patch("api_weather.requests.get", side_effect=api_weather.requests.exceptions.Timeout):
        result = api_weather.fetch_weather("Baghdad")

    assert result is None


def test_fetch_weather_connection_error():
    with patch("api_weather.requests.get", side_effect=api_weather.requests.exceptions.ConnectionError):
        result = api_weather.fetch_weather("Baghdad")

    assert result is None


def test_fetch_weather_unexpected_status_code():
    fake_response = MagicMock()
    fake_response.status_code = 500

    with patch("api_weather.requests.get", return_value=fake_response):
        result = api_weather.fetch_weather("Baghdad")

    assert result is None
