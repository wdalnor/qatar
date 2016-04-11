from django.test import TestCase

from rango.models import Category





class CategoryMethodTests(TestCase):

	def test_slug_line_creation(self):
		cat = Category("random string category")
		cat.save()
		self.assertEqual(cat.slug,"random-string-category")


 