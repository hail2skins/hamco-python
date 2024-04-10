from django.urls import path

# Import the views from the notes app
from . import views

urlpatterns = [
    
    # Path to the create view
    path('create', views.create, name='create'),
    
]
