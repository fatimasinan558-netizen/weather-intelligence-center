import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city_name):
    """
    تجيب بيانات الطقس الحالية لمدينة معينة.
    ترجع dictionary فيه البيانات، أو None إذا صار خطأ.
    """
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric",  # عشان الحرارة تطلع بالسيلزيوس
        "lang": "ar"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()
            return {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "condition": data["weather"][0]["description"]
            }
        elif response.status_code == 404:
            print(f"خطأ: المدينة '{city_name}' غير موجودة.")
            return None
        else:
            print(f"خطأ غير متوقع من الـ API: كود {response.status_code}")
            return None

    except requests.exceptions.Timeout:
        print("خطأ: انتهت مهلة الاتصال (Timeout). حاول مرة ثانية.")
        return None
    except requests.exceptions.ConnectionError:
        print("خطأ: ماكو اتصال بالإنترنت.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"خطأ غير متوقع: {e}")
        return None
