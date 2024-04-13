from django.test import Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from hamco.base_test import BaseTest
from notes.models import Note

class CreateNoteTemplateTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.client.login(username='testuser', password='12345')
        self.url = reverse('create')
        self.initial_note_count = Note.objects.count()

    def test_create_note_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'notes/create.html')

    def test_create_note_form_displayed(self):
        response = self.client.get(self.url)
        self.assertContains(response, '<form method="post" enctype="multipart/form-data">')
        self.assertContains(response, '<button type="submit" class="btn btn-primary">Create Note</button>')
        
    def test_create_note_post(self):
        response = self.client.post(self.url, {'title': 'Test Note', 'content': 'Test Content'})
        final_note_count = Note.objects.count()
        self.assertEqual(response.status_code, 302)  # Check if redirect happened
        self.assertEqual(final_note_count, self.initial_note_count + 1)  # Check if a new note was created
        
    def test_create_note_form_fields(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'name="title"')  # Check for title field
        self.assertContains(response, 'name="content"')  # Check for content field

    def test_create_note_without_title(self):
        response = self.client.post(self.url, {'content': 'Test Content'})
        final_note_count = Note.objects.count()
        self.assertContains(response, 'This field is required.')  # Check for error message
        self.assertEqual(final_note_count, self.initial_note_count)  # Check no new note was created

    def test_create_note_without_content(self):
        response = self.client.post(self.url, {'title': 'Test Note'})
        final_note_count = Note.objects.count()
        self.assertContains(response, 'This field is required.')  # Check for error message
        self.assertEqual(final_note_count, self.initial_note_count)  # Check no new note was created
        
    def test_create_note_unauthenticated(self):
        # Create a new client that is not logged in
        client = Client()
        response = client.get(self.url)
        self.assertRedirects(response, '/auth/login?next=' + self.url)  # Check if redirect to login page happened

# Testing the detail template
class NoteDetailTemplateTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.note = self.notes[0]  # Get the first note created in BaseTest
        self.url = reverse('details', args=[self.note.id])  # Replace 'detail' with your actual URL name

    def test_note_detail_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'notes/details.html')

    def test_note_content_displayed(self):
        response = self.client.get(self.url)
        self.assertContains(response, self.note.content)  # Check if note content is displayed

    def test_update_delete_links_for_authenticated_user(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.url)
        update_url = reverse('update', args=[self.note.id])  # Get the actual update URL
        delete_url = reverse('delete', args=[self.note.id])  # Get the actual delete URL
        self.assertContains(response, f'href="{update_url}"')  # Check for update link
        self.assertContains(response, f'action="{delete_url}"')  # Check for delete link
        
# testing the history view
class NoteHistoryTemplateTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.url = reverse('history')  # Replace 'history' with your actual URL name

    def test_note_history_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'notes/history.html')

    def test_notes_displayed(self):
        response = self.client.get(self.url)
        for note in self.notes:
            self.assertContains(response, note.title)  # Check if note title is displayed
            self.assertContains(response, note.content)  # Check if note content is displayed

    def test_update_delete_links_for_authenticated_user(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.url)
        for note in self.notes:
            update_url = reverse('update', args=[note.id])  # Get the actual update URL
            delete_url = reverse('delete', args=[note.id])  # Get the actual delete URL
            self.assertContains(response, f'href="{update_url}"')  # Check for update link
            self.assertContains(response, f'action="{delete_url}"')  # Check for delete link    
        
        
# Testing the update template
class UpdateNoteTemplateTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.client.login(username='testuser', password='12345')
        self.note = self.notes[0]  # Get the first note created in BaseTest
        self.url = reverse('update', args=[self.note.id])  # Replace 'update' with your actual URL name

    def test_update_note_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'notes/update.html')

    def test_update_note_form_displayed(self):
        response = self.client.get(self.url)
        self.assertContains(response, '<form method="post" enctype="multipart/form-data">')
        self.assertContains(response, '<button type="submit" class="btn btn-primary">Update Note</button>')

    def test_update_note_form_fields(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'name="title"')  # Check for title field
        self.assertContains(response, 'name="content"')  # Check for content field

    def test_update_note_without_title(self):
        response = self.client.post(self.url, {'content': 'Test Content'})
        self.assertContains(response, 'This field is required.')  # Check for error message

    def test_update_note_without_content(self):
        response = self.client.post(self.url, {'title': 'Test Note'})
        self.assertContains(response, 'This field is required.')  # Check for error message

    def test_update_note_unauthenticated(self):
        # Create a new client that is not logged in
        client = Client()
        response = client.get(self.url)
        self.assertRedirects(response, '/auth/login?next=' + self.url)  # Check if redirect to login page happened     
        
# Testing the delete template
class DeleteNoteTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.client.login(username='testuser', password='12345')
        self.note = self.notes[0]  # Get the first note created in BaseTest
        self.initial_note_count = Note.objects.count()

    def test_delete_note_from_history(self):
        url = reverse('delete', args=[self.note.id])  # Replace 'delete' with your actual URL name
        response = self.client.post(url)
        final_note_count = Note.objects.count()
        self.assertEqual(response.status_code, 302)  # Check if redirect happened
        self.assertEqual(final_note_count, self.initial_note_count - 1)  # Check if a note was deleted

    def test_delete_note_from_details(self):
        url = reverse('delete', args=[self.note.id])  # Replace 'delete' with your actual URL name
        response = self.client.post(url)
        final_note_count = Note.objects.count()
        self.assertEqual(response.status_code, 302)  # Check if redirect happened
        self.assertEqual(final_note_count, self.initial_note_count - 1)  # Check if a note was deleted


    
        
    