from django.shortcuts import render, redirect

# Create your views here.


def view_cart(request):
    """ A view to return the index page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:  # this is to check if a product with sizes is being added
        if item_id in list(cart.keys()):
            # if item is in the cart
            if size in cart[item_id]['items_by_size'].keys():
                # if item and size exist in the cart increment qty
                cart[item_id]['items_by_size'][size] += quantity
            else:
                cart[item_id]['items_by_size'][size] = quantity
        else:
            # if item is not in cart add it
            cart[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
