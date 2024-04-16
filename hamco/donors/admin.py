from django.contrib import admin

# Import the Donor and Contribution models
from .models import Donor, Contribution

# Register your models here.
# This is the simplest way to register a model with the admin site
admin.site.register(Donor)
admin.site.register(Contribution)
