from django.shortcuts import render
# Import redirect from django.shortcuts
from django.shortcuts import redirect

# Import login_required decorator to protect views
from django.contrib.auth.decorators import login_required

# Import forms models
from .forms import NoteForm

# Import the Note model
from .models import Note

# Import the User model from Django
from django.contrib.auth.models import User

# Create your views here.

# Create the create view
# This view will be protected by the login_required decorator
# This decorator will redirect the user to the login page if they are not authenticated
@login_required(login_url='login')
def create(request):
    
    # Create a form instance from the NoteForm class
    form = NoteForm()
    
    # Check if the request method is POST
    if request.method == 'POST':
        
        # Create a form instance from the NoteForm class with the data from the POST request
        form = NoteForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            
            # Hold a note to retrieve the user
            note = form.save(commit=False)
            
            # Set the user to the current user
            note.user = request.user
            
            # Create a new note with the title and content from the form
            note.save()
            
            # Redirect the user to the home page
            return redirect('')
    
    # Context dictionary to pass the form to the template
    context = {
        'form': form
    }
    
    return render(request, 'notes/create.html', context)
