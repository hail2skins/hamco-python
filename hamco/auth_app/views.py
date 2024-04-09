from django.shortcuts import render

# import django auth views to add context menu
from django.contrib.auth.views import LoginView

# Create your views here.

# Login view not technically needed but need it for the context menu
def login(request, *args, **kwargs):
    extra_context = {
        'title': 'Hamco IS',
        'company': 'Hamco Internet Solutions',
    }
    return LoginView.as_view(extra_context=extra_context)(request, *args, **kwargs)
