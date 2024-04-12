from django.test import Client, TestCase
from django.urls import reverse
from hamco.base_test import BaseTest
 # Import the Note model
from notes.models import Note

class HomeViewTest(BaseTest):
    def setUp(self):
        # Every test needs access to the request factory and the client.
        self.client = Client()

    # Test the home view
    def test_home_view(self):
        response = self.client.get(reverse('')) # reverse() is used to generate the URL for the view

        # Check that the response has a status code of 200
        self.assertEqual(response.status_code, 200)

        # Check that the correct template was used
        self.assertTemplateUsed(response, 'website/index.html')

        # Check that the response context contains the expected keys
        self.assertIn('title', response.context)
        self.assertIn('company', response.context)
        self.assertIn('heading', response.context)
        self.assertIn('latest_notes', response.context)

        # Check that the context data contains the latest 5 notes
        latest_notes = Note.objects.order_by('-created_at')[:5]
        # Content assertion didn't work. I had to convert the queryset to a set of ids
        # and compare the ids. The set() function is an unordered collection of unique elements.
        latest_notes_ids = set(note.id for note in latest_notes)
        response_notes_ids = set(note.id for note in response.context['latest_notes'])
        # debug print
        #print(response.context['latest_notes'])
        #print(latest_notes)
        self.assertEqual(latest_notes_ids, response_notes_ids)
        
    # Test the about view
    def test_about_view(self):
        response = self.client.get(reverse('about'))

        # Check that the response has a status code of 200
        self.assertEqual(response.status_code, 200)

        # Check that the correct template was used
        self.assertTemplateUsed(response, 'website/about.html')

        # Check that the response context contains the expected keys
        self.assertIn('heading', response.context)
 
  