from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm, OrderForm
from .models import OrderItem, Order

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                quantity=cd['quantity'],
                override_quantity=cd['override'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True})
    return render(request, 'cart/detail.html', {'cart': cart})

@login_required
def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        return redirect('product_list')
        
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            
            # Clear the cart
            cart.clear()
            
            # Set the order in the session
            request.session['order_id'] = order.id
            
            # Redirect to order confirmation
            return redirect('order_complete')
    else:
        # Pre-fill the form with user information if available
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email
            }
        form = OrderForm(initial=initial_data)
    
    return render(request, 'checkout/checkout.html', {
        'cart': cart,
        'form': form
    })

def order_complete(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'checkout/order_complete.html', {'order': order})