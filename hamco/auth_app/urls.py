from django.urls import path, include

# Import the views from the website app
from . import views

import django.contrib.auth.urls

urlpatterns = [
    
    # path to django auth urls
    path('', include('django.contrib.auth.urls')),
    
    # path to the login view
    path('login', views.login_view, name='login'),
    
    # path to the register view
    path('register/', views.register, name='register'),
        
    
]