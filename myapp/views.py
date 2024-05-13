from django.shortcuts import render
from .models import *
from .forms import *

def cityWeather(request):
    cities = CityWeather.objects.all()
    form = CityForm()
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form, 'cities':cities}
    return render(request, 'myapp/weather.html', context)
