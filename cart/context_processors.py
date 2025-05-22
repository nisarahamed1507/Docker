from .cart import Cart

def cart_total_amount(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        total_bill = 0.0
        for key, value in request.session.items():
            if key == 'cart':
                for item_id, item_details in value.items():
                    total_bill += float(item_details['price']) * int(item_details['quantity'])
        return {'cart_total_amount': total_bill}
    else:
        return {'cart_total_amount': 0}