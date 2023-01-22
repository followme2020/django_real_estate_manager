from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class LeadUser(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    message = models.TextField()

    def __str__(self):
        return f'{self.firstname},{self.lastname}'

    def get_absolute_url(self):
        return reverse('lead-detail', args=[str(self.id)])
