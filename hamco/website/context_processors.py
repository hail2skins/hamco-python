# context_processors.py
# This file will contain common context that I want to apply throughout the app.  
# I have to make a chance to settings to include this file in the TEMPLATES setting.

# Import the Slogan model from the slogans app
from slogans.models import Slogan

# common_context provides title and company to all templates
def common_context(request):
    return {
        'title': 'Hamco Internet Solutions',
        'company': 'Hamco Internet Solutions',
    }
    
# random_slogan provides a random slogan to all templates
#it uses the Slogan model class method get_random
def random_slogan(request):
    return {'random_slogan': Slogan.get_random()}