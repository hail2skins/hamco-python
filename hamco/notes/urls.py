from django.urls import path

# Import the views from the notes app
from . import views

urlpatterns = [
    
    # Path to the create view
    path('create', views.create, name='create'),
    # Path to the notes view
    path('history', views.notes, name='history'),
    # Path to the details view of a note
    path('details/<int:pk>', views.details, name='details'),
    # Path to the update view of a note
    path('update/<int:pk>', views.update, name='update'),
    # Path to the delete view of a note
    path('delete/<int:pk>', views.delete, name='delete'),
    
]
