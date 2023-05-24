from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True, 'style': {'input_type': 'password'}}}
    
    def create(self, validated_data):
        """Creates and returns a new user"""
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user

