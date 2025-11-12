import requests

def get_weather(city="Tunisia", api_key="TA_CLE_API"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    data = requests.get(url).json()
    return data['main']['temp']
