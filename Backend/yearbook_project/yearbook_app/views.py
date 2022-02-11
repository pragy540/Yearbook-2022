from django.shortcuts import render
from werkzeug import Response
from . import serializers 
from rest_framework import viewsets  
from rest_framework.decorators import api_view    
from rest_framework.response import Response
from . import models         



# class ProfileView(viewsets.ModelViewSet):  
#     # serializer_class = ProfileSerializer 
#     # queryset = Profile.objects.all()     

@api_view(['GET'])    
def profile_disp(request):
    data = models.Profile.objects.all()
    data_serializer = serializers.ProfileSerializer(data, many=True)
    return Response(data_serializer.data)

@api_view(['POST'])
def add_person(request):
    req_data = request.data
    person, created = models.Profile.objects.get_or_create(rollno = req_data['rollno'])
    if created:
        person.name = req_data['name']
        person.save()
        person_serializer = serializers.ProfileSerializer(person)
        return Response(person_serializer.data)
    else:
        return Response({'status': 'Person already created'})