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
            return redirect('history')
    
    # Context dictionary to pass the form to the template
    context = {
        'form': form,
        'heading': 'Tell it',
    }
    
    return render(request, 'notes/create.html', context)

# Create the notes view
# This view will have a list of all notes showing Title, Content and Created_at
# Created at will be formated to show month, day and year only
# Content will be truncated to 30 words
# This will be shown in a bootstrap striped table
def notes(request):
    
    # Retrieve all notes
    notes = Note.objects.all()
    
    # Context dictionary to pass the notes to the template
    context = {
        'notes': notes,
        'heading': 'The Mother Load',
        
    }
    
    return render(request, 'notes/history.html', context)

# Create the details view
# This view will show the details of a note with the title, content, created_at
# Created at will be formated to show month, day and year only
# This view will need to be dynamic and take a note id as a parameter
def details(request, pk):
        
    # try/except block to handle the case where the note does not exist
    try:
        # get the note by primary key
        note = Note.objects.get(id=pk)
    except Note.DoesNotExist:
        # If the note does not exist redirect to the history page
        return redirect('history')
    
    # Context dictionary to pass the note to the template
    context = {
        'note': note,
        'heading': note.title,
        'view': 'details',
    }
    
    # Render the details template with the context
    return render(request, 'notes/details.html', context)

# Create the update view
# This view will allow the user to update a note with a form
# This view will need to be dynamic and take a note id as a parameter
# This view will be protected by the login_required decorator
@login_required(login_url='login')
def update(request, pk):
        
        # try/except block to handle the case where the note does not exist
        try:
            # get the note by primary key
            note = Note.objects.get(id=pk)
        except Note.DoesNotExist:
            # If the note does not exist redirect to the history page
            return redirect('history')
        
        # Check if the note user is not the current user
        if note.user != request.user:
            # If the note user is not the current user redirect to the history page
            return redirect('history')
        
        # Create a form instance from the NoteForm class with the instance of the note
        form = NoteForm(instance=note)
        
        # Check if the request method is POST
        if request.method == 'POST':
            
            # Create a form instance from the NoteForm class with the data from the POST request and the instance of the note
            form = NoteForm(request.POST, instance=note)
            
            # Check if the form is valid
            if form.is_valid():
                
                # Save the form
                form.save()
                
                # Redirect the user to the history page
                return redirect('history')
        
        # Context dictionary to pass the form to the template
        context = {
            'form': form,
            'heading': 'It wasn not quite right?',
            'subheading': 'Make it better.',
        }
        
        # Render the update template with the context
        return render(request, 'notes/update.html', context)
    
# Create the delete view
# This view will allow the user to delete a note
# This view will need to be dynamic and take a note id as a parameter
# This view will be protected by the login_required decorator
@login_required(login_url='login')
def delete(request, pk):
        
        # try/except block to handle the case where the note does not exist
        try:
            # get the note by primary key
            note = Note.objects.get(id=pk)
        except Note.DoesNotExist:
            # If the note does not exist redirect to the history page
            return redirect('history')
        
        # Check if the note user is not the current user
        if note.user != request.user:
            # If the note user is not the current user redirect to the history page
            return redirect('history')
        
        # Check if the request method is POST
        if request.method == 'POST':
            
            # Delete the note
            note.delete()
            
            # Redirect the user to the history page
            return redirect('history')
        
        # Context dictionary to pass the note to the template
        context = {
            'note': note,
            'heading': 'Some things are better left unsaid',
            'subheading': 'This can not be undone.',
        }
        
        # Render the delete template with the context
        return render(request, 'notes/history.html')