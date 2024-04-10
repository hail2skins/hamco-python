from django.shortcuts import render

# Create your views here.
def home(request):

    # Context dictionary
    context = {
        'title': 'Hamco Internet Solutions',
        'company': 'Hamco Internet Solutions',
        'heading': 'Stuff I Talk About',
        'subheading': 'That will not get me fired.',
    }

    return render(request, 'website/index.html', context)

