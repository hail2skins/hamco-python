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
        # model_bakery randomizes things like content, text, slogan in models so you can keep it short.
        # Create a user
        cls.user = baker.make(User, username='testuser', is_superuser=True)
        cls.user.set_password('12345')  # Set the password explicitly
        cls.user.save()

        # Create 6 notes
        cls.notes = baker.make(Note, _quantity=6, user=cls.user)

        # Create 3 slogans
        # Here I expressly made slogan as Slogan 1, 2, 3 as this may be needed in the future.
        cls.slogans = [baker.make(Slogan, slogan=f'Slogan {i+1}', user=cls.user) for i in range(3)]
        
        # Create a second user
        cls.user2 = baker.make(User, username='testuser2')
        cls.user2.set_password('12345')
        cls.user2.save()
        
        # Create 1 note for the second user -- NOT POSSIBLE NOW AS USER IS NOT SUPERUSER
        # cls.note2 = baker.make(Note, user=cls.user2)
        