from django.db import models

# Create your models here.

class Alien(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    nativePlanet=models.CharField(max_length=100)
    weight=models.IntegerField()
    height=models.IntegerField()
    language=models.CharField(max_length=100)

    def __str__(self):
        return self.name