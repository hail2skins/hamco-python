from django.shortcuts import render

# Create your views here.

# Create the create view
def create(request):
    
    return render(request, 'notes/create.html')
