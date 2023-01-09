from django.db import models
from django.urls import reverse


class Resort(models.Model):
    name = models.CharField(max_length=200, help_text='Enter resort name (ex: Caesar blue)')

    def __str__(self):
        return self.name


class Building(models.Model):
    id = models.IntegerField(primary_key=True, help_text='Unique id')
    name = models.CharField(max_length=50, unique=True, help_text='Enter name of building (ex: Markus)')
    building_number = models.IntegerField(help_text='Building number')
    resort = models.ForeignKey('Resort', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return f'{self.name},{self.building_number}'

    def get_absolute_url(self):
        return reverse('building-detail', args=[str(self.id)])

    class Meta:
        ordering = ['name']


class Apartment(models.Model):
    id = models.AutoField(primary_key=True)
    building = models.ForeignKey('Building', on_delete=models.RESTRICT, null=True)
    apartment_number = models.CharField(max_length=20)
    floor = models.CharField(max_length=20)
    bedrooms = models.CharField(max_length=20)
    covered_gross = models.DecimalField(verbose_name='Covered Gross Area', decimal_places=2, max_digits=9, null=True)
    balcony = models.DecimalField(verbose_name='Balcony area sqm', decimal_places=2, max_digits=7, null=True)
    position = models.CharField(max_length=20)
    price_in_gbp = models.IntegerField(null=True)

    def get_absolute_url(self):
        return reverse('apartment-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.apartment_number}, {self.floor}'

    class Meta:
        ordering = ['id']
