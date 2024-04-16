from django.db import models

# Create your models here.

'''
Donors model

The Donor model will have required fields last_name, first_name, street_number, street_name,
city, state, zip_code, and needs_review. The needs_review field will be a boolean field that
defaults to False.

This model will relate heavily to the Contributions model below. 

'''
class Donor(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    street_number = models.CharField(max_length=255, null=True)  # Allow NULL values
    street_name = models.TextField(null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=2, null=True)
    zip_code = models.CharField(max_length=5, null=True)
    needs_review = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def full_address(self):
        return f"{self.street_number} {self.street_name}, {self.city}, {self.state} {self.zip_code}"
    
'''
Contributions model

The Contributions model will have required fields donor, date, and amount. The donor field will
be a foreign key to the Donor model. The date field will be a DateField and the amount field will
be a DecimalField with a max_digits of 10 and a decimal_places of 2.

'''
class Contribution(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"${self.amount} from {self.donor} on {self.date}"