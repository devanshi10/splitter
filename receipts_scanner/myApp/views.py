from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.response import Response

# Create your views here.

class UserView(APIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def post(self, request) -> Response:
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            name = serializer.validated_data.get('first_name')
            return Response(serializer.validated_data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)