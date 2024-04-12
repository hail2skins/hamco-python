from django.test import TestCase
from notes.forms import NoteForm

class NoteFormTest(TestCase):
    def test_form_valid(self):
        # Create a form instance with some example data
        form = NoteForm({
            'title': 'Test Note',
            'content': 'This is a test note.',
        })

        # Check that the form is valid
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        # Create a form instance with some example data that is missing the title
        form = NoteForm({
            'content': 'This is a test note.',
        })

        # Check that the form is not valid
        self.assertFalse(form.is_valid())

        # Check that the form is indicating that the title field is required
        self.assertEqual(form.errors['title'], ['This field is required.'])