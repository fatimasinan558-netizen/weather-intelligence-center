# Thresholds قابلة للتعديل
THRESHOLDS = {
    "hot_temperature": 40,
    "cold_temperature": 10,
    "high_wind": 10,
    "low_humidity": 20,
    "high_humidity": 70,
    "rain": 5
}


def check_thresholds(weather_data):
    """
    يفحص حالة الطقس ويولد التنبيهات حسب الـ thresholds.
    """
    alerts = []

    temperature = weather_data["temperature"]
    humidity = weather_data["humidity"]
    wind_speed = weather_data["wind_speed"]
    rain = weather_data.get("rain", 0)

    if temperature >= THRESHOLDS["hot_temperature"]:
        alerts.append("تحذير: درجة الحرارة عالية جدًا")

    if temperature <= THRESHOLDS["cold_temperature"]:
        alerts.append("تحذير: درجة الحرارة منخفضة جدًا")

    if humidity <= THRESHOLDS["low_humidity"]:
        alerts.append("تحذير: الرطوبة منخفضة جدًا")

    if humidity >= THRESHOLDS["high_humidity"]:
        alerts.append("تحذير: الرطوبة مرتفعة جدًا")

    if wind_speed >= THRESHOLDS["high_wind"]:
        alerts.append("تحذير: سرعة الرياح عالية")

    if rain >= THRESHOLDS["rain"]:
        alerts.append("تحذير: توجد أمطار")

    return alerts


def generate_recommendations(weather_data):
    """
    يولد توصيات حسب حالة الطقس.
    """
    recommendations = []

    temperature = weather_data["temperature"]
    humidity = weather_data["humidity"]
    wind_speed = weather_data["wind_speed"]
    rain = weather_data.get("rain", 0)

    if temperature >= THRESHOLDS["hot_temperature"]:
        recommendations.append("يفضل تجنب التعرض المباشر للشمس وشرب الماء.")

    if temperature <= THRESHOLDS["cold_temperature"]:
        recommendations.append("يفضل ارتداء ملابس دافئة.")

    if humidity <= THRESHOLDS["low_humidity"]:
        recommendations.append("يفضل شرب كمية كافية من الماء.")

    if wind_speed >= THRESHOLDS["high_wind"]:
        recommendations.append("يفضل تجنب الأماكن المفتوحة أثناء الرياح القوية.")

    if rain >= THRESHOLDS["rain"]:
        recommendations.append("يفضل حمل مظلة وتجنب الطرق التي قد تتجمع فيها المياه.")

    if not recommendations:
        recommendations.append("الطقس مناسب بشكل عام.")

    return recommendations


def weather_rule_engine(weather_data):
    """
    Rule Engine يجمع التنبيهات والتوصيات.
    """
    alerts = check_thresholds(weather_data)
    recommendations = generate_recommendations(weather_data)

    return {
        "alerts": alerts,
        "recommendations": recommendations
    }


def decision_table(alerts):
    """
    Decision Table للتعامل مع وجود أكثر من تنبيه.
    """
    if not alerts:
        return "لا توجد تنبيهات"

    if len(alerts) >= 3:
        return "حالة خطرة: توجد عدة تنبيهات، يفضل اتخاذ احتياطات عالية."

    if len(alerts) == 2:
        return "حالة تحتاج انتباه: يوجد أكثر من تنبيه."

    return "حالة تحتاج انتباه: يوجد تنبيه واحد."


def calculate_risk_score(weather_data):
    """
    يحسب درجة المخاطر من 0 إلى 100.
    """
    score = 0

    temperature = weather_data["temperature"]
    humidity = weather_data["humidity"]
    wind_speed = weather_data["wind_speed"]
    rain = weather_data.get("rain", 0)

    if temperature >= THRESHOLDS["hot_temperature"]:
        score += 40
    elif temperature >= 35:
        score += 25

    if temperature <= THRESHOLDS["cold_temperature"]:
        score += 20

    if humidity <= THRESHOLDS["low_humidity"]:
        score += 30
    elif humidity >= THRESHOLDS["high_humidity"]:
        score += 20

    if wind_speed >= THRESHOLDS["high_wind"]:
        score += 30

    if rain >= THRESHOLDS["rain"]:
        score += 10

    return min(score, 100)


def calculate_comfort_score(weather_data):
    """
    يحسب درجة ملاءمة الطقس من 0 إلى 100
    مع مراعاة الحرارة والرطوبة والرياح والأمطار.
    """
    score = 100
    reasons = []

    temperature = weather_data["temperature"]
    humidity = weather_data["humidity"]
    wind_speed = weather_data["wind_speed"]
    rain = weather_data.get("rain", 0)

    if temperature >= THRESHOLDS["hot_temperature"]:
        score -= 40
        reasons.append("الحرارة مرتفعة جدًا")
    elif temperature >= 35:
        score -= 25
        reasons.append("الحرارة مرتفعة")
    elif temperature <= THRESHOLDS["cold_temperature"]:
        score -= 25
        reasons.append("الحرارة منخفضة جدًا")

    if humidity <= THRESHOLDS["low_humidity"]:
        score -= 20
        reasons.append("الرطوبة منخفضة جدًا")
    elif humidity >= THRESHOLDS["high_humidity"]:
        score -= 20
        reasons.append("الرطوبة مرتفعة جدًا")

    if wind_speed >= THRESHOLDS["high_wind"]:
        score -= 20
        reasons.append("الرياح قوية")

    if rain >= THRESHOLDS["rain"]:
        score -= 15
        reasons.append("وجود أمطار يقلل من الراحة")

    score = max(score, 0)

    if not reasons:
        explanation = "الطقس مريح بشكل عام ولا توجد عوامل رئيسية تقلل من الراحة."
    else:
        explanation = "انخفضت درجة الراحة بسبب: " + "، ".join(reasons) + "."

    return {
        "score": score,
        "explanation": explanation
    }