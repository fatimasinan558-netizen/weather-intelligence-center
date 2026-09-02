import json
import os
from datetime import datetime

SNAPSHOTS_FILE = "data/snapshots.json"


def load_snapshots():
    """
    تقرا كل السجلات المحفوظة من ملف JSON.
    ترجع list فارغة إذا الملف مو موجود أو تالف.
    """
    if not os.path.exists(SNAPSHOTS_FILE):
        return []

    try:
        with open(SNAPSHOTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("تحذير: ملف السجلات تالف أو فارغ، رح نبدي بسجل جديد.")
        return []


def save_snapshot(weather_data):
    """
    تضيف سجل طقس جديد (snapshot) لملف JSON مع الوقت الحالي.
    """
    snapshots = load_snapshots()

    new_snapshot = {
        "city": weather_data["city"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": weather_data["temperature"],
        "feels_like": weather_data["feels_like"],
        "humidity": weather_data["humidity"],
        "wind_speed": weather_data["wind_speed"],
        "condition": weather_data["condition"]
    }

    snapshots.append(new_snapshot)

    os.makedirs("data", exist_ok=True)

    with open(SNAPSHOTS_FILE, "w", encoding="utf-8") as f:
        json.dump(snapshots, f, ensure_ascii=False, indent=2)

    print(f"تم حفظ سجل الطقس لمدينة {weather_data['city']}.")


def get_snapshots_by_city(city_name):
    """
    ترجع كل السجلات المحفوظة لمدينة معينة.
    """
    snapshots = load_snapshots()
    return [s for s in snapshots if s["city"].lower() == city_name.lower()]
