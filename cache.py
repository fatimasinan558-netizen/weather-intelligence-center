import time

_cache = {}

CACHE_DURATION = 600  # 10 دقائق


def get_cached(city):
    city = city.lower()

    if city in _cache:
        data, saved_time = _cache[city]

        if time.time() - saved_time < CACHE_DURATION:
            return data

        del _cache[city]

    return None


def save_to_cache(city, weather_data):
    city = city.lower()
    _cache[city] = (weather_data, time.time())