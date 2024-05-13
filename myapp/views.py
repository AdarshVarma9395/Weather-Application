from django.shortcuts import render
import requests
from .models import *
from .forms import *

def cityWeather(request):
    cities = CityWeather.objects.all()
    api_key = '3dbe66b1080011fc05328679ffa841f3'
    form = CityForm()
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()

    weather_data = []
    for city in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city.name}&appid={api_key}'
        city_weather = requests.get(url).json()

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon'],
            'humidity' : city_weather['main']['humidity'],
            'pressure' : city_weather['main']['pressure'],  # Corrected 'perssure' to 'pressure'
        }
        weather_data.append(weather)

    context = {'form':form, 'weather_data':weather_data}

    return render(request, 'myapp/weather.html', context)
