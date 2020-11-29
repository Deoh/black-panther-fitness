from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from workout_class.models import WorkoutClass

"""Shopping cart functionality"""


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    """Add to cart data"""
    for session_key, item_data in cart.items():
        item_type, item_id = session_key.split("/")
        """
        check to see if item has size by checking if item data is not
        an integer
        """
        if isinstance(item_data, int):
            if item_type == 'workout_class':
                item = get_object_or_404(WorkoutClass, pk=item_id)
            else:
                item = get_object_or_404(Product, pk=item_id)

            total += item_data * item.price
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'item_type': item_type,
                'quantity': item_data,
                'product': item,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    """
    free delivery if spending is more than the amount
    specified in the free delivery threshold in settings.py
    """
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
