# base_test.py
from model_bakery import baker
from django.test import TestCase
from notes.models import Note
from slogans.models import Slogan
# Import the Django user model
from django.contrib.auth.models import User

class BaseTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        cls.user = baker.make(User, username='testuser')

        # Create 6 notes
        cls.notes = baker.make(Note, _quantity=6, user=cls.user)

        # Create 3 slogans
        cls.slogans = [baker.make(Slogan, slogan=f'Slogan {i+1}', user=cls.user) for i in range(3)]
        