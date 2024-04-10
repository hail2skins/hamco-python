from django.db import models

# Import django User model
from django.contrib.auth.models import User

# Import markdown
import markdown

# importing BeautifulSoup to convert from html markdown to text for the history page
from bs4 import BeautifulSoup

# Create your models here.
'''
Create the Note model
The note model will have required fields title, a text field for content that can't be null.
I want created_at (when created), updated_at (when updated) and deleted_at (when deleted) fields
I need the note created by the current user so I will create a foreign key to the User model
The user model is provided by Django in this instance and is imported above.

The created_at field will be automatically set to the current date and time when the note is created
The updated_at field will be automatically set to the current date and time when the note is updated
The deleted_at field will be set to the current date and time when the note is deleted but this will be done in the views.py file
'''
class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    # content_as_html method
    # This method will return the content as HTML
    # Utilizing markdown as imported above
    def content_as_html(self):
        return markdown.markdown(self.content, extensions=['fenced_code', 'codehilite'], extension_configs={'codehilite': {'use_pygments': False}})
    
   # content_as_text method
    # This method will return the content as text
    # Utilizing BeautifulSoup as imported above
    # to remove the markdown from the raw content allowing it to look better in the table
    def content_as_text(self):
        html_content = self.content_as_html()
        soup = BeautifulSoup(html_content, "html.parser")
        plain_text_content = soup.get_text()
        return plain_text_content