from django.shortcuts import render
import requests
from pprint import pprint
import json
from .models import City
from .forms import CityForm


def index(request):
    appid = '8c6e2d9436acbde37b29064e40e3ac3d'
    URL = 'https://api.openweathermap.org/data/2.5/weather?q={city},&units=metric&appid=' + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    all_cities = []
    for city in cities:
        response = requests.get(URL.format(city=city.name)).json()
        city_info = {
            'city': city.name,
            'temp': response['main']['temp'],
            'icon': response['weather'][0]['icon'],
        }
        all_cities.append(city_info)
    context = {'all_info': all_cities, 'form': form}
    return render(request, 'WeatherApp/index.html', context)


def about(request):

    context = {}
    return render(request, 'WeatherApp/about.html', context)
