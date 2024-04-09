from django.urls import path, include

# Import the views from the website app
from . import views

import django.contrib.auth.urls

urlpatterns = [
    
    # path to django auth urls
    path('', include('django.contrib.auth.urls')),
    
    # path to the login view
    path('login', views.login, name='login'),
        
    
]