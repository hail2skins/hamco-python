from django.shortcuts import render

# Import the Note model to run queryset 
# Note models are in the notes app, not the website app
from notes.models import Note

# Create your views here.
def home(request):
    
    # Queryset for the last five notes ordered by created_at
    latest_notes = Note.objects.order_by('-created_at')[:5]

    # Context dictionary
    context = {
        'title': 'Hamco Internet Solutions',
        'company': 'Hamco Internet Solutions',
        'heading': 'Stuff I Talk About',
        'latest_notes': latest_notes,
    }

    return render(request, 'website/index.html', context)

