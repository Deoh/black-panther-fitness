from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product
from workout_class.models import WorkoutClass

# Create your views here.


def view_cart(request):
    """ A view to return the index page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_type, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    if item_type == 'workout_class':
        item = get_object_or_404(WorkoutClass, pk=item_id)
    else:
        item = get_object_or_404(Product, pk=item_id)

    session_key = "/".join((item_type, item_id))

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if item_type == 'product' and 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:  # this is to check if a product with sizes is being added
        if session_key in cart.keys():
            # if item is in the cart
            if size in cart[session_key]['items_by_size'].keys():
                # if item and size exist in the cart increment qty
                cart[session_key]['items_by_size'][size] += quantity
                messages.success(
                    request, f'Updated size {size.upper()} {item.name} quantity to {cart[session_key]["items_by_size"][size]}')
            else:
                cart[session_key]['items_by_size'][size] = quantity
                messages.success(
                    request, f'Added size {size.upper()} {item.name} to your cart')
        else:
            # if item is not in cart add it as a dictionary
            cart[session_key] = {'items_by_size': {size: quantity}}
            messages.success(
                request, f'Added size {size.upper()} {item.name} to your cart')
    else:
        if session_key in list(cart.keys()):
            cart[session_key] += quantity
            messages.success(
                request, f'Updated {item.name} quatity to {cart[session_key]}')
        else:
            cart[session_key] = quantity
            messages.success(request, f'Added {item.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_type, item_id):
    """
    Adjust the quantity of the specified product to the specified amount
    """
    if item_type == 'workout_class':
        item = get_object_or_404(WorkoutClass, pk=item_id)
    else:
        item = get_object_or_404(Product, pk=item_id)

    session_key = "/".join((item_type, item_id))

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            cart[session_key]['items_by_size'][size] = quantity
            messages.success(
                request, f'Updated size {size.uppeitem.name} quantity to {cart[session_key]["items_by_size"][size]}')
        else:
            del cart[session_key]['items_by_size'][size]
            if not cart[session_key]['items_by_size']:
                cart.pop(session_key)
                messages.success(
                    request, f'Removed size {size.upper()} {item.name} from your cart')
    else:
        if quantity > 0:
            cart[session_key] = quantity
            messages.success(
                request, f'Updated {item.name} quantity to {cart[session_key]}')
        else:
            cart.pop(session_key)
            messages.success(request, f'Removed {item.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_type, item_id):
    """ Remove the item from the shopping cart """

    try:
        if item_type == 'workout_class':
            item = get_object_or_404(WorkoutClass, pk=item_id)
        else:
            item = get_object_or_404(Product, pk=item_id)

        session_key = "/".join((item_type, item_id))
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[session_key]['items_by_size'][size]
            if not cart[session_key]['items_by_size']:
                cart.pop(session_key)
            messages.success(
                request, f'Removed size {size.upper()} {item.name} from your cart')
        else:
            cart.pop(session_key)
            messages.success(request, f'Removed {item.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
