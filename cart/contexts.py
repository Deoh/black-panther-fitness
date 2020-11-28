from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from workout_class.models import WorkoutClass

"""Shopping cart functionality"""


def cart_contents(request):

    cart_items = []
    total = 0
    total_for_class = 0
    product_count = 0
    cart = request.session.get('cart', {})

    """Add to cart data"""
    for item_id, item_data in cart.items():
        # check to see if item has size by checking if item data is an integer
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            workout_class = get_object_or_404(WorkoutClass, pk=item_id)
            total += item_data * product.price
            total_for_class+= item_data * workout_class.price
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'workout_class': workout_class,
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

    grand_total = delivery + total + total_for_class

    context = {
        'cart_items': cart_items,
        'total': total,
        'total_for_class': total_for_class,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
