from django.db import models

# Import django user model
from django.contrib.auth.models import User

# Create your models here.

# Create a Slogan model
# This model will store the slogans. It will only have one field, slogan, which is a CharField.
# Slogans will associate with the user who created it by foreign key relationship.
# And Slogans will have a created_at field to store the date and time the slogan was created.
class Slogan(models.Model):
    slogan = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.slogan
