from django.test import TestCase, Client

# Create your tests here.
from django.test import RequestFactory

# Import base test data setup
from hamco.base_test import BaseTest

# Import the Note model
from notes.models import Note

# Import the Slogan model
from slogans.models import Slogan

# Create a TemplateTest class 
class TemplateTest(BaseTest):
    def setUp(self):
        self.client = Client()

    # Test the homepage contains the title and company from the common_context context processor
    # Test the homepage contains the heading and latest notes from the home view
    def test_homepage_contains_expected_content(self):
        response = self.client.get('/')
        # debug print
        print(response.content)
        
        # Simple assertions
        self.assertContains(response, '<title>Hamco Internet Solutions</title>', html=True)
        self.assertContains(response, '<a class="navbar-brand" href="index.html">Hamco Internet Solutions</a>', html=True)
        self.assertContains(response, '<h1>Stuff I Talk About</h1>', html=True)
        
        # Query all notes ordering by created at for most recent
        all_notes = list(Note.objects.order_by('-created_at'))
        latest_five_notes = all_notes[:5]  # Get the latest 5 notes
        for note in latest_five_notes:
            self.assertContains(response, note.title) # assert the note tile for the latest five is on the page
        # Check that the response does not contain the 6th note
        if len(all_notes) > 5:  # Check if there are more than 5 notes
            sixth_note = all_notes[5]
            self.assertNotContains(response, sixth_note.title)
        
        # Test if the page contains any of the slogans text from any of the possible slogans
        self.assertTrue(any(slogan.slogan in str(response.content) for slogan in self.slogans))
        
    # Test the about page contains the title and company from the common_context context processor
    def test_about_contains_expected_content(self):
        response = self.client.get('/about/')
        
        # simple assertions
        self.assertContains(response, '<title>Hamco Internet Solutions</title>', html=True)
        self.assertContains(response, '<a class="navbar-brand" href="index.html">Hamco Internet Solutions</a>', html=True)
        self.assertContains(response, '<h1>I knew you were curious!</h1>', html=True)
        
        # Test if the page contains any of the slogans text from any of the possible slogans
        self.assertTrue(any(slogan.slogan in str(response.content) for slogan in self.slogans))
                
   