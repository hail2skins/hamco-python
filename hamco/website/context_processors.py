# context_processors.py
# This file will contain common context that I want to apply throughout the app.  
# I have to make a chance to settings to include this file in the TEMPLATES setting.

# Import the Slogan model from the slogans app
from slogans.models import Slogan

# import os to faciliate random_image function
import os

# import settings to faciliate the random_image function
from django.conf import settings

# import random to facilitate the random_image function
import random

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

# random_image provides a random image to all templates
# it uses the session to store the random image per page
# so as a user navigates the site, the image will differ per page but stay that way for sesson
# The masthead images are stored in the static/images/main folder
def random_image(request):
    # Get random image
    page = request.path  # Get the URL of the current page
    if page not in request.session:
        images_dir = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'main')  # Change 'main' to the name of your new folder
        images = [f for f in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir, f))]
        request.session[page] = random.choice(images)
    return {'random_image': request.session[page]}