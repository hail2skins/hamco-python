from django.shortcuts import render

# Create your views here.
def home(request):

    # Context dictionary
    context = {
        'title': 'Hamco IS',
        'company': 'Hamco Internet Solutions',
    }

    return render(request, 'website/index.html', context)

