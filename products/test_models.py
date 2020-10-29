from django.test import TestCase
from .models import Category, Product

# Create your tests here.


class TestModels(TestCase):

    def test_category_string_method_returns_name(self):
        category = Category.objects.create(
            name='new category', friendly_name='new friendly name')
        self.assertEqual(str(category), 'new category',)
        self.assertEqual(str(category.get_friendly_name()),
                         'new friendly name')

    def test_product_string_method_returns_name(self):
        product = Product.objects.create(name='new product', price=10)
        self.assertEqual(str(product), 'new product')
