from django.shortcuts import render

# Import login_required decorator to protect views
from django.contrib.auth.decorators import login_required

# Create your views here.

# Create the create view
# This view will be protected by the login_required decorator
# This decorator will redirect the user to the login page if they are not authenticated
@login_required(login_url='login')
def create(request):
    
    return render(request, 'notes/create.html')
