from django.test import TestCase, Client

# Create your tests here.
from django.test import RequestFactory

# Create a TemplateTest class 
class TemplateTest(TestCase):
    def setUp(self):
        self.client = Client()

    # Test the homepage contains the title and company from the common_context context processor
    def test_homepage_contains_title_and_company(self):
        response = self.client.get('/')
        self.assertContains(response, '<title>Hamco Internet Solutions</title>', html=True)
        self.assertContains(response, '<a class="navbar-brand" href="index.html">Hamco Internet Solutions</a>', html=True)
