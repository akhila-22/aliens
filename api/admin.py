from django.contrib import admin
from .models import Alien
# Register your models here.

@admin.register(Alien)
class AlienAdmin(admin.ModelAdmin):
    list_display=['name','age','nativePlanet','weight','height','language']