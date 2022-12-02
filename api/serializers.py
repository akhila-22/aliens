from rest_framework import serializers
from .models import Alien

class AlienSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alien
        fields = '__all__'


    

