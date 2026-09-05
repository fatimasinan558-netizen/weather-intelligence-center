def check_thresholds(weather_data):
    alerts = []

    if weather_data["temperature"] >= 40:
        alerts.append("تحذير: درجة الحرارة عالية جدًا")

    if weather_data["humidity"] <= 20:
        alerts.append("تحذير: الرطوبة منخفضة جدًا")

    if weather_data["wind_speed"] >= 10:
        alerts.append("تحذير: سرعة الرياح عالية")

    return alerts


def calculate_risk_score(weather_data):
    score = 0

    if weather_data["temperature"] >= 40:
        score += 40
    elif weather_data["temperature"] >= 35:
        score += 25

    if weather_data["humidity"] <= 20:
        score += 30

    if weather_data["wind_speed"] >= 10:
        score += 30

    return min(score, 100)


def calculate_comfort_score(weather_data):
    score = 100

    temperature = weather_data["temperature"]
    humidity = weather_data["humidity"]

    if temperature >= 40:
        score -= 40
    elif temperature >= 35:
        score -= 25
    elif temperature >= 30:
        score -= 10

    if humidity < 20 or humidity > 70:
        score -= 20

    return max(score, 0)