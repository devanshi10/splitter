from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from .models import UserProfile, ExpenseGroup
from .serializers import UserProfileSerializer, GroupSerializer, DebtSerializer
from rest_framework.response import Response

# Create your views here.

class UserView(APIView):
    #queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def post(self, request) -> Response:
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #name = serializer.validated_data.get('first_name')
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request) -> Response:
        users = UserProfile.objects.all()
        emails = [user.email for user in users]
        if emails == []:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(emails, status=status.HTTP_201_CREATED)
    
class CreateGroupView(APIView):
    serializer_class = GroupSerializer
    def post(self, request):
        all_users = []
        for user_email in request.data.get('members', []):
            all_users.append(UserProfile.objects.get(email=user_email).id)
        request.data['members'] = all_users
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request) -> Response:
        groups = ExpenseGroup.objects.all()
        names = [group.group_name for group in groups]
        if names == []:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(names, status=status.HTTP_201_CREATED)
    
class CreateDebtView(APIView):
    serializer_class = DebtSerializer

    def post(self, request) -> Response:
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #name = serializer.validated_data.get('first_name')
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

     