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
        self.assertEqual(str(note), note.title)

    def test_note_update(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', password='12345') # Create a user
        note = Note.objects.create(title="A simple title", content="Some content", user=user) # Create a note
        note.title = "Updated title" # Update the title
        note.save() # Save the changes
        retrieved_note = Note.objects.get(title="Updated title") # Retrieve the updated note
        self.assertEqual(retrieved_note.title, "Updated title")

    def test_note_deletion(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', password='12345') # Create a user
        note = Note.objects.create(title="A simple title", content="Some content", user=user) # Create a note
        note.delete() # Delete the note
        with self.assertRaises(Note.DoesNotExist): # Assert that the note does not exist
            Note.objects.get(title="A simple title")

    def test_retrieve_note_by_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', password='12345') # Create a user
        note = Note.objects.create(title="A simple title", content="Some content", user=user) # Create a note
        retrieved_note = Note.objects.filter(user=user) # Retrieve the note by user
        self.assertEqual(retrieved_note.first(), note) # Assert that the retrieved note is equal to the created note # Assert that the title is updated # Assert that the string representation of the note is equal to the title of the note
        
        
# View tests


        