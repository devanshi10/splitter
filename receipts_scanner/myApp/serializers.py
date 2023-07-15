from rest_framework import serializers
from .models import UserProfile, Debt, Group, Expense

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

    
class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ('borrower', 'reciever', 'amount')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'group_name', 'members')

    def get_members(self, obj):
        return list(obj.members.values_list('email', flat=True))


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('expense_name','selectedGroup','paidBy','splitbtw','amount')

