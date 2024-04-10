from django.test import TestCase
from .models import Note
from django.contrib.auth import get_user_model
from django.db import IntegrityError

# Model tests

# NoteModelTest class
# test_note_creation method tests the creation of a note by creating a user and a note
# The test asserts that the note content is equal to the content that was created
class NoteModelTest(TestCase):
    def test_note_creation(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', password='12345') # Create a user
        note = Note.objects.create(title="A simple title", content="Some content", user=user) # Create a note
        retrieved_note = Note.objects.get(title="A simple title") # Retrieve the note
        self.assertEqual(retrieved_note.content, "Some content") # Assert that the content is equal to the content that was created
        self.assertEqual(str(note), note.title) # Assert that the string representation of the note is equal to the title of the note
        
        
# View tests


        