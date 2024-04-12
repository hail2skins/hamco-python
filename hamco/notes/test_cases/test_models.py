from django.test import TestCase
from model_bakery import baker
from notes.models import Note

class NoteModelTest(TestCase):
    # The setUp method is a special method that Django runs before each test method.
    # Here, we're using it to create a Note instance that will be used in the test methods.
    def setUp(self):
        self.note = baker.make(Note, content='**bold text**')

    # This test method checks that the content_as_html method of the Note model works correctly.
    # It does this by comparing the output of the method to the expected HTML string.
    def test_content_as_html(self):
        # The expected HTML string. This is what we expect the content_as_html method to return.
        expected_html = '<p><strong>bold text</strong></p>'
        # We call the content_as_html method and compare its output to the expected HTML string.
        # If they are not equal, the test will fail.
        self.assertEqual(self.note.content_as_html().strip(), expected_html)

    # This test method checks that the content_as_text method of the Note model works correctly.
    # It does this by comparing the output of the method to the expected text string.
    def test_content_as_text(self):
        # The expected text string. This is what we expect the content_as_text method to return.
        expected_text = 'bold text'
        # We call the content_as_text method and compare its output to the expected text string.
        # If they are not equal, the test will fail.
        self.assertEqual(self.note.content_as_text().strip(), expected_text)