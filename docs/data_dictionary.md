# Data Dictionary

## 1. مخرجات fetch_weather() — من api_weather.py

الدالة `fetch_weather(city_name)` ترجع dictionary بهذا الشكل عند النجاح:

```json
{
  "city": "Baghdad",
  "temperature": 32.95,
  "feels_like": 31.55,
  "humidity": 27,
  "wind_speed": 5.14,
  "condition": "clear sky"
}
```

| الحقل | النوع | الوصف |
|---|---|---|
| city | string | اسم المدينة كما يرجعها الـ API |
| temperature | float | درجة الحرارة بالسيلزيوس |
| feels_like | float | درجة الحرارة المحسوسة بالسيلزيوس |
| humidity | int | نسبة الرطوبة (%) |
| wind_speed | float | سرعة الرياح (m/s) |
| condition | string | وصف نصي للحالة الجوية |

ترجع `None` عند أي خطأ (مدينة غير موجودة، انقطاع اتصال، timeout، خطأ سيرفر).

## 2. ملف data/snapshots.json — من storage.py

كل سجل (Snapshot) مخزّن بهذا الشكل داخل list واحدة:

```json
[
  {
    "city": "بغداد",
    "timestamp": "2026-09-03 01:21:54",
    "temperature": 32.95,
    "feels_like": 31.55,
    "humidity": 27,
    "wind_speed": 5.14,
    "condition": "سماء صافية"
  }
]
```

| الحقل | النوع | الوصف |
|---|---|---|
| city | string | اسم المدينة |
| timestamp | string | تاريخ ووقت الحفظ (YYYY-MM-DD HH:MM:SS) |
| temperature | float | درجة الحرارة وقت الحفظ |
| feels_like | float | الحرارة المحسوسة وقت الحفظ |
| humidity | int | الرطوبة وقت الحفظ |
| wind_speed | float | سرعة الرياح وقت الحفظ |
| condition | string | وصف الحالة الجوية وقت الحفظ |

## الدوال المتاحة من storage.py

- `save_snapshot(weather_data)` → تضيف سجل جديد للملف
- `load_snapshots()` → ترجع كل السجلات (list of dict)
- `get_snapshots_by_city(city_name)` → ترجع سجلات مدينة معينة فقط
