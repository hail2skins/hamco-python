from django.contrib import admin

# Import truncator
from django.utils.text import Truncator

# Register your models here.
from . models import Note

# Register the Note model with the admin site
# This is the simplest way to register a model with the admin site
#admin.site.register(Note)


# Register the Note model with the admin site with customization
# Customizing the admin interface for the note model
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'truncated_content', 'created_at', 'updated_at', 'deleted_at',)
    list_filter = ('created_at', 'updated_at', 'deleted_at',)
    search_fields = ('title', 'content',)
    #prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('created_at',)
    
    # Custom method to truncate the content
    def truncated_content(self, obj):
        return Truncator(obj.content).words(15, truncate='...')
    truncated_content.short_description = 'Content'