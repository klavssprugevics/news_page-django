from django.conf import settings
from datetime import datetime
import requests

def time(request):
    return {'time': datetime.now().strftime("%H:%M")}

def weather(request):
    api_key = settings.WEATHER_KEY
    all_ok = True

    weather = requests.get('http://api.weatherapi.com/v1/current.json?key=' + api_key + '&q=Riga&aqi=no', params=request.GET)
    if weather.status_code == 200:
        info = weather.json()
        return {'weather':info}

    else:
        return {'weather':'No weather data'} 