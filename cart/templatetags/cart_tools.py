from django import template

"""
Custom template filter
Note: create an empty file called __init__ .py
which will ensure that this directory is treated as a Python package
making the cart_tools module available for imports and to use in templates.
check out 'Custom template tags and filters' on the django website
"""

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):  # calculate the product subtotal
    return price * quantity
