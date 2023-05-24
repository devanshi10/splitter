
from django.urls import path
from .views import UserView



urlpatterns = [
    path('userprofile', UserView.as_view(), name='userprofile_detail'),
   
]