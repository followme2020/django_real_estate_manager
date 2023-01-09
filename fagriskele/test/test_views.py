# from django.test import TestCase
# from django.urls import reverse
# from fagriskele.models import Apartment
#
#
# class ApartmentListViewTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # Create 13 apartments for pagination tests
#         number_of_apartments = 14
#
#         for apartment_id in range(number_of_apartments):
#             Apartment.objects.create(
#                 apartment_number=f'A- {apartment_id}',
#                 floor=f'5th {apartment_id}',
#             )
#
#     def test_view_url_exists_at_desired_location(self):
#         response = self.client.get('/fagriskele/apartments/')
#         self.assertEqual(response.status_code, 200)
#
#     def test_view_url_accessible_by_name(self):
#         response = self.client.get(reverse('apartments'))
#         self.assertEqual(response.status_code, 200)
#
#     def test_view_uses_correct_template(self):
#         response = self.client.get(reverse('apartments'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, '/fagriskele/apartment_list.html')
#
#     def test_pagination_is_ten(self):
#         response = self.client.get(reverse('apartments'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTrue('is_paginated' in response.context)
#         self.assertTrue(response.context['is_paginated'] == True)
#         self.assertEqual(len(response.context['apartment_list']), 10)
#
#     def test_lists_all_authors(self):
#         # Get second page and confirm it has (exactly) remaining 4 items
#         response = self.client.get(reverse('apartments')+'?page=2')
#         self.assertEqual(response.status_code, 200)
#         self.assertTrue('is_paginated' in response.context)
#         self.assertTrue(response.context['is_paginated'] == True)
#         self.assertEqual(len(response.context['apartment_list']), 4)
