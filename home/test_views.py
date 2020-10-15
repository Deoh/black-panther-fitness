from django.test import TestCase

# Create your tests here.

"""
We want to test not only that our views return a successful HTTP response
and that they're using the proper templates.
But also what they can do. in this case specifically
adding, editing, toggling and deleting items.
"""

class TestViews(TestCase):

    def test_get_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  # testing for a successful HTTP response
        self.assertTemplateUsed(response, 'home/index.html')  # To confirm the view uses the correct template.

