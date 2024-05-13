from django.forms import ModelForm
from .models import *

class CityForm(ModelForm):
    class Meta:
        model = CityWeather
        fields = '__all__'