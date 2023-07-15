from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
import string
import random
import uuid


# Create your models here.
class UserProfileManager(BaseUserManager):
    """ Manager for user profiles """

    def create_user(self, email, password=None, **extra_fields):
        """Create a new user profile"""
        if not email:
            raise ValueError('Invalid Email')
        # normalize email, convert second half to lowercase
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_profiles',  # Added related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_profiles',  # Added related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email
    
class Debt(models.Model):
    borrower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='from_user')
    reciever = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='to_user')
    amount = models.IntegerField()


class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group_name = models.CharField(max_length=255, unique=True)
    debts = models.ManyToManyField(Debt, null=True)
    members = models.ManyToManyField(UserProfile)

    def __str__(self):
        return self.group_name

class Expense(models.Model):
    expense_name = models.CharField(max_length=255)
    selectedGroup = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='selected_group')
    paidBy = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='paid_by')
    splitbtw = models.ManyToManyField(UserProfile)
    amount = models.FloatField()





