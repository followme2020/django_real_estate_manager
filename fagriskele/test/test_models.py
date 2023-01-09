from django.test import TestCase
from fagriskele.models import Apartment


class ApartmentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Apartment.objects.create(id=3, apartment_number='K-59', floor='5th')

    def test_apartment_number_label(self):
        apartment = Apartment.objects.get(id=3)
        field_label = apartment._meta.get_field('apartment_number').verbose_name
        self.assertEqual(field_label, 'apartment number')

    def test_floor_label(self):
        apartment = Apartment.objects.get(id=3)
        field_label = apartment._meta.get_field('floor').verbose_name
        self.assertEqual(field_label, 'floor')

    def test_apartment_number_max_length(self):
        apartment = Apartment.objects.get(id=3)
        max_length = apartment._meta.get_field('apartment_number').max_length
        self.assertEqual(max_length, 20)

    def test_object_name_is_apartment_number_comma_floor(self):
        apartment = Apartment.objects.get(id=3)
        expected_object_name = str(apartment)
        self.assertEqual(str(apartment), expected_object_name)

    def test_get_absolute_url(self):
        apartment = Apartment.objects.get(id=3)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(apartment.get_absolute_url(), '/fagriskele/apartment/3')
