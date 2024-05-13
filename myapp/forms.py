from django.forms import ModelForm
from .models import *

class CityForm(ModelForm):
    class Meta:
        models = CityWeather
        fields = '__all__'