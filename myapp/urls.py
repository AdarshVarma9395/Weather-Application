from django.urls import path
from .views import *

urlpatterns = [
    path("", cityWeather, name='home')
]
