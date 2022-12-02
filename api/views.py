from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Alien
from .serializers import AlienSerializer
from django.http import HttpResponse
def index(request):
    return HttpResponse('Hello')

@api_view(['GET','POST'])

def alien_api(request):

    if request.method=='GET':
        ali = Alien.objects.all()
        serializer=AlienSerializer(ali,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=AlienSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['PUT','DELETE'])

def alien_api2(request,id):
    if request.method=='PUT':
        try:
            aliobj=Alien.objects.get(id=id)
            serializer=AlienSerializer(aliobj,data=request.data,partial=True)
            if  serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Exception as e:
            return Response({'status' : 403,'errors':serializer.errors,'message': 'invalid id'})
        


    elif request.method=='DELETE':
        try:

            alienob=Alien.objects.get(id=id)
            alienob.delete()
            return Response({'message':'deleted'})
        except Exception as e:
            print(e)
            return Response({'message':'invalid id'})
            
    



