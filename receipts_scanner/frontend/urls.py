
from django.urls import path, include
from .views import index


urlpatterns = [
    path('',index),
    path('create',index),
    path('creategroup',index),
    path('showgroups',index),
    path('createexpense',index),
    path('showexpense',index)
    #path('', TemplateView.as_view(template_name='index.html')),
]
