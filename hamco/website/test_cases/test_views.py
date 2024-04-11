from django.test import TestCase, Client

# Create your tests here.
from django.test import RequestFactory
from website.context_processors import common_context


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
    