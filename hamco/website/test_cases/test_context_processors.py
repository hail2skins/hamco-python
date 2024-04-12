from django.test import TestCase, Client

# Create your tests here.
from django.test import RequestFactory
from website.context_processors import common_context, random_image

# Import os to facilitate random_image function
import os

# Import settings to facilitate the random_image function
from django.conf import settings


# Test the common_context context processor from context_processors.py
# Returns a dictionary with title and company keys
def test_common_text_returns_correct_dictionary():
    # Arrange
    factory = RequestFactory()
    request = factory.get('/')

    # Act
    result = common_context(request)

    # Assert
    assert isinstance(result, dict)
    assert 'title' in result
    assert 'company' in result
    assert result['title'] == 'Hamco Internet Solutions'
    assert result['company'] == 'Hamco Internet Solutions'
    
def test_random_image_returns_dictionary_with_random_image_key():
    # Initialize
    request = type('Request', (object,), {'path': '/test_page', 'session': {}})()
    
    # Invoke
    result = random_image(request)
    
    # Assert
    assert isinstance(result, dict)
    assert 'random_image' in result.keys()

    # Check that the 'random_image' value is a string
    assert isinstance(result['random_image'], str)

    # Check that the 'random_image' value corresponds to an existing file
    images_dir = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'main')
    assert os.path.isfile(os.path.join(images_dir, result['random_image']))
    