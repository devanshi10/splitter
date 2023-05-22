from django.shortcuts import render
from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer

# Create your views here.

class UserView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

