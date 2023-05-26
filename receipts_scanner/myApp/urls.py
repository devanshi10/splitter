
from django.urls import path
from .views import UserView, CreateGroupView, CreateDebtView



urlpatterns = [
    path('userprofile', UserView.as_view(), name='userprofile_detail'),
    path('creategroup', CreateGroupView.as_view()),
    path('createdebt', CreateDebtView.as_view())
   
]