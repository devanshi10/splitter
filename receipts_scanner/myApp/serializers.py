from rest_framework import serializers
from .models import UserProfile, Debt, Group, Expense
import uuid

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
    members = serializers.SlugRelatedField(
        many=True,
        slug_field='email',
        queryset=UserProfile.objects.all()
    )
    
    class Meta:
        model = Group
        fields = ('group_name', 'members')

    def get_members(self, obj):
        return list(obj.members.values_list('email', flat=True))
    
    def create(self, validated_data):
     
        members_data = validated_data.pop('members', [])
        group = Group.objects.create(**validated_data)
        for member_data in members_data:
            member_obj = UserProfile.objects.get(email = member_data)
            group.members.add(member_obj)
        

        return group

   

class ExpenseSerializer(serializers.ModelSerializer):
    splitbtw = serializers.SlugRelatedField(
        many=True,
        slug_field='email',
        queryset=UserProfile.objects.all()
    )
    paidBy= serializers.SlugRelatedField(
        slug_field='email',
        queryset=UserProfile.objects.all()
    )
    selectedGroup = serializers.SlugRelatedField(slug_field='group_name', queryset=Group.objects.all())
    class Meta:
        model = Expense
        fields = ('expense_name','selectedGroup','paidBy','splitbtw','amount')

    def create(self, validated_data):
     
        members_data = validated_data.pop('splitbtw', [])
        validated_data['selectedGroup'] = Group.objects.get(group_name = validated_data['selectedGroup'])
        validated_data['paidBy'] = UserProfile.objects.get(email = validated_data["paidBy"])
        expense = Expense.objects.create(**validated_data)
        for member_data in members_data:
            member_obj = UserProfile.objects.get(email = member_data)
            expense.splitbtw.add(member_obj)
        

        return expense
