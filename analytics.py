from storage import get_snapshots_by_city


def calculate_statistics(city_name):
    """
    تحسب المعدل وأعلى وأقل درجة حرارة ورطوبة ورياح لمدينة معينة.
    """
    snapshots = get_snapshots_by_city(city_name)

    if not snapshots:
        return None

    temperatures = [s["temperature"] for s in snapshots]
    humidity = [s["humidity"] for s in snapshots]
    wind_speeds = [s["wind_speed"] for s in snapshots]

    return {
        "city": city_name,
        "temperature": {
            "average": sum(temperatures) / len(temperatures),
            "max": max(temperatures),
            "min": min(temperatures)
        },
        "humidity": {
            "average": sum(humidity) / len(humidity),
            "max": max(humidity),
            "min": min(humidity)
        },
        "wind_speed": {
            "average": sum(wind_speeds) / len(wind_speeds),
            "max": max(wind_speeds),
            "min": min(wind_speeds)
        }
    }


def calculate_temperature_trend(city_name):
    """
    تحدد اتجاه درجة الحرارة بناءً على السجلات المحفوظة.
    """
    snapshots = get_snapshots_by_city(city_name)

    if len(snapshots) < 2:
        return "بيانات غير كافية"

    previous_temperature = snapshots[-2]["temperature"]
    latest_temperature = snapshots[-1]["temperature"]

    if latest_temperature > previous_temperature:
        return "صاعد"
    elif latest_temperature < previous_temperature:
        return "نازل"
    else:
        return "مستقر"