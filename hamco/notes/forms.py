# Import django forms for ModelForm
from django import forms

# Import widgets for form fields
from django.forms.widgets import TextInput, Textarea

# Import models
# Import the Note model
from .models import Note

# Import the user model from Django
from django.contrib.auth.models import User


# Create the NoteForm class
# This class will inherit from the ModelForm class
# This class will create a form for the Note model
# The form will have fields title and content
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'content': Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}),
        }