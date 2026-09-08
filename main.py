from api_weather import fetch_weather
from storage import save_snapshot
from analytics import calculate_statistics, calculate_temperature_trend
from rules import weather_rule_engine, decision_table, calculate_comfort_score

if __name__ == "__main__":
    city = input("اكتب اسم المدينة: ")
    weather_data = fetch_weather(city)

    if weather_data:
        print("\n--- بيانات الطقس ---")
        print(f"المدينة: {weather_data['city']}")
        print(f"الحرارة: {weather_data['temperature']}°C")
        print(f"الإحساس بالحرارة: {weather_data['feels_like']}°C")
        print(f"الرطوبة: {weather_data['humidity']}%")
        print(f"سرعة الرياح: {weather_data['wind_speed']} m/s")
        print(f"الحالة: {weather_data['condition']}")

        save_snapshot(weather_data)

        # التنبيهات والتوصيات
        rule_results = weather_rule_engine(weather_data)
        print("\n--- التنبيهات ---")
        if rule_results["alerts"]:
            for alert in rule_results["alerts"]:
                print(f"⚠️  {alert}")
        else:
            print("لا توجد تنبيهات.")

        print("\n--- التوصيات ---")
        for rec in rule_results["recommendations"]:
            print(f"👉 {rec}")

        print("\n--- تقييم الحالة ---")
        print(decision_table(rule_results["alerts"]))

        # Weather Comfort Score
        comfort = calculate_comfort_score(weather_data)
        print("\n--- درجة ملاءمة الطقس (Comfort Score) ---")
        print(f"الدرجة: {comfort['score']}/100")
        print(f"السبب: {comfort['explanation']}")

        # الإحصائيات (يحتاج سجل تاريخي كافي)
        stats = calculate_statistics(weather_data["city"])
        if stats:
            print("\n--- إحصائيات المدينة (من السجل المحفوظ) ---")
            print(f"متوسط الحرارة: {stats['temperature']['average']:.1f}°C")
            print(f"أعلى حرارة: {stats['temperature']['max']}°C")
            print(f"أقل حرارة: {stats['temperature']['min']}°C")

            trend = calculate_temperature_trend(weather_data["city"])
            print(f"اتجاه الحرارة: {trend}")
