from django.db import models

class CityWeather(models.Model):
    name = models.CharField( max_length=200)

    def __str__(self):
        return self.name
    

# 3dbe66b1080011fc05328679ffa841f3