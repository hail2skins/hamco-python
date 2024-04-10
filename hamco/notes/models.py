from django.db import models

# Import django User model
from django.contrib.auth.models import User

# Create your models here.
'''
Create the Note model
The note model will have required fields title, a text field for content that can't be null.
I want created_at (when created), updated_at (when updated) and deleted_at (when deleted) fields
I need the note created by the current user so I will create a foreign key to the User model
The user model is provided by Django in this instance and is imported above.

The created_at field will be automatically set to the current date and time when the note is created
The updated_at field will be automatically set to the current date and time when the note is updated
The deleted_at field will be set to the current date and time when the note is deleted but this will be done in the views.py file
'''
class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title