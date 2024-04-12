from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model # this is idiomatic way to get the user model
from notes.models import Note
from notes.forms import NoteForm
from hamco.base_test import BaseTest

# Testing the create view
class CreateViewTest(BaseTest):
    # The setUp method is a special method that Django runs before each test method.
    # Here, we're using it to create a test user and log them in.
    def setUp(self):
        self.client = Client()
        self.client.login(username='testuser', password='12345')
        self.original_count = self.user.note_set.count()  # Store the count of notes

    # This test method checks that the create view uses the correct template.
    def test_create_view_uses_correct_template(self):
        response = self.client.get(reverse('create'))
        self.assertTemplateUsed(response, 'notes/create.html')

    # This test method checks that the create view creates a new note when it receives a valid POST request.
    def test_create_view_creates_new_note(self):
        #original_count = self.user.note_set.count()
        
        response = self.client.post(reverse('create'), {
            'title': 'Test Note',
            'content': 'This is a test note.',
        })
        # Check that a note was created
        self.assertEqual(self.user.note_set.count(), self.original_count + 1)
        # Check that the note has the correct title
        self.assertEqual(self.user.note_set.last().title, 'Test Note')

    # This test method checks that the create view redirects the user to the correct URL after creating a note.
    def test_create_view_redirects_after_post(self):
        response = self.client.post(reverse('create'), {
            'title': 'Test Note',
            'content': 'This is a test note.',
        })
        self.assertRedirects(response, reverse('history'))

    # This test method checks that the create view adds the note to the correct user's notes.
    def test_create_view_adds_note_to_correct_user(self):
        # Store the user's current note count
        #original_count = self.user.note_set.count()
        
        response = self.client.post(reverse('create'), {
           'title': 'Test Note',
          'content': 'This is a test note.',
        })
        
        # Check that the count of notes has increased by 1
        self.assertEqual(self.user.note_set.count(), self.original_count + 1)
        # Check that the note has the correct title
        self.assertEqual(self.user.note_set.last().title, 'Test Note')

    # This test method checks that the create view passes a form into the template context.
    def test_create_view_passes_form_to_template(self):
        response = self.client.get(reverse('create'))
        self.assertIsInstance(response.context['form'], NoteForm)
        
# Testing the notes history view
class NotesViewTest(BaseTest):
    def setUp(self):
        super().setUp()  # Call setUp of BaseTest to get the user and client

    def test_notes_view_uses_correct_template(self):
        response = self.client.get(reverse('history'))
        self.assertTemplateUsed(response, 'notes/history.html')

    def test_notes_view_returns_all_notes(self):
        response = self.client.get(reverse('history'))
        self.assertEqual(len(response.context['notes']), Note.objects.count())

    def test_notes_view_passes_correct_context(self):
        response = self.client.get(reverse('history'))
        self.assertEqual(response.context['heading'], 'The Mother Load')
        
class DetailsViewTest(BaseTest):
    def setUp(self):
        super().setUp()  # Call setUp of BaseTest to get the user and client

    def test_details_view_uses_correct_template(self):
        note_id = self.user.note_set.first().id
        response = self.client.get(reverse('details', args=[note_id]))
        self.assertTemplateUsed(response, 'notes/details.html')

    def test_details_view_returns_correct_note(self):
        note = self.user.note_set.first()
        response = self.client.get(reverse('details', args=[note.id]))
        self.assertEqual(response.context['note'], note)

    def test_details_view_redirects_for_invalid_note_id(self):
        invalid_note_id = self.user.note_set.last().id + 10000000
        response = self.client.get(reverse('details', args=[invalid_note_id]))
        self.assertRedirects(response, reverse('history'))

    def test_details_view_passes_correct_context(self):
        note = self.user.note_set.first()
        response = self.client.get(reverse('details', args=[note.id]))
        self.assertEqual(response.context['heading'], note.title)
        self.assertEqual(response.context['view'], 'details')
        
class UpdateViewTest(BaseTest):
    def setUp(self):
        super().setUp()  # Call setUp of BaseTest to get the user and client
        self.client.login(username='testuser', password='12345')  # Log in the user
        self.note = self.user.note_set.first()  # Get a note to update

    def test_update_view_uses_correct_template(self):
        response = self.client.get(reverse('update', args=[self.note.id]))
        self.assertTemplateUsed(response, 'notes/update.html')

    def test_update_view_redorects_for_invalid_note_id(self):
        invalid_note_id = self.user.note_set.last().id + 1
        response = self.client.get(reverse('update', args=[invalid_note_id]))
        self.assertRedirects(response, reverse('history'))

    def test_update_view_updates_note(self):
        response = self.client.post(reverse('update', args=[self.note.id]), {
            'title': 'Updated Note',
            'content': 'This is an updated note.',
        })
        self.note.refresh_from_db()  # Refresh the note from the database
        self.assertEqual(self.note.title, 'Updated Note')
        self.assertEqual(self.note.content, 'This is an updated note.')

    def test_update_view_redirects_after_post(self):
        response = self.client.post(reverse('update', args=[self.note.id]), {
            'title': 'Updated Note',
            'content': 'This is an updated note.',
        })
        self.assertRedirects(response, reverse('history'))
        

class DeleteViewTest(BaseTest):
    def setUp(self):
        super().setUp()  # Call setUp of BaseTest to get the user and client
        self.client.login(username='testuser', password='12345')  # Log in the user
        self.note = self.user.note_set.first()  # Get a note to delete

    def test_delete_view_redirects_for_invalid_note_id(self):
        invalid_note_id = self.user.note_set.last().id + 1
        response = self.client.get(reverse('delete', args=[invalid_note_id]))
        self.assertRedirects(response, reverse('history'))

    def test_delete_view_redirects_for_wrong_user(self):
        # Try to delete the second user's note as the first user
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('delete', args=[self.note2.id]))
        self.assertRedirects(response, reverse('history'))

    def test_delete_view_deletes_note(self):
        response = self.client.post(reverse('delete', args=[self.note.id]))
        with self.assertRaises(Note.DoesNotExist):
            Note.objects.get(id=self.note.id)  # This should raise Note.DoesNotExist because the note has been deleted

    def test_delete_view_redirects_after_post(self):
        response = self.client.post(reverse('delete', args=[self.note.id]))
        self.assertRedirects(response, reverse('history'))