from decimal import Decimal
from django.conf import settings

"""Shopping bag functionality"""


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0

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

    contents = {
        'bag_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return contents