from api_weather import fetch_weather

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
