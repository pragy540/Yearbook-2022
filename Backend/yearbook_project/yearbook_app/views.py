from django.shortcuts import render
from .serializers import ProfileSerializer 
from rest_framework import viewsets      
from .models import Profile                

class ProfileView(viewsets.ModelViewSet):  
    serializer_class = ProfileSerializer   
    queryset = Profile.objects.all()     
