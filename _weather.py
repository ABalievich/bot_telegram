import requests

descriptions = {'clear sky': 'чистое небо',
                'scattered clouds': 'рассеянные облака',
                'broken clouds': 'облачно',
                'overcast clouds': 'пасмурно',
                'light rain': 'небольшой дождь',
                'moderate rain': 'умеренный дождь',
                'thunderstorm': 'гроза',
                'thunderstorm with light rain': 'гроза с небольшим дождем'}


def weather(city):
    appid = 'e785298bef3a12878186fdcb2c7abeac'
    url_weather = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={appid}'
    resp_weather = requests.get(url_weather)
    weather_json = resp_weather.json()

    city_info = f"Город: {city}"
    city_info += f"\nОписание: {descriptions[weather_json['weather'][0]['description']]}"
    city_info += f"\nТемпература: {weather_json['main']['temp']}\u2103"
    city_info += f"\nВлажность: {weather_json['main']['humidity']}%"
    city_info += f"\nСкорость ветра: {weather_json['wind']['speed']} м/с"                

    return city_info
