from django.contrib import admin

# Register your models here.
from . models import Slogan

# Register the Slogan model with the admin site
# This is the simplest way to register a model with the admin site
#admin.site.register(Slogan)


# Register the Slogan model with the admin site with customization
# Customizing the admin interface for the Slogan model
@admin.register(Slogan)
class SloganAdmin(admin.ModelAdmin):
    list_display = ('id', 'slogan', 'created_at',)
    #list_filter = ('created_at', 'updated_at', 'deleted_at',)
    search_fields = ('slogan',)
    #prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('created_at',)
    