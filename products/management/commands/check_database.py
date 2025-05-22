import os
import django
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Display data from the database to check if records exist'

    def handle(self, *args, **options):
        # Display orders
        try:
            from cart.models import Order, OrderItem
            orders = Order.objects.all()
            self.stdout.write(self.style.SUCCESS(f'Found {orders.count()} orders in database'))
            
            for order in orders:
                self.stdout.write(f'Order ID: {order.id}, Name: {order.first_name} {order.last_name}, Email: {order.email}')
                order_items = OrderItem.objects.filter(order=order)
                self.stdout.write(f'  Items: {order_items.count()}')
                for item in order_items:
                    self.stdout.write(f'    - {item.product.name}: {item.quantity} x ${item.price}')
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error checking orders: {e}'))
        
        # Display products
        try:
            from products.models import Product
            products = Product.objects.all()
            self.stdout.write(self.style.SUCCESS(f'\nFound {products.count()} products in database'))
            for product in products[:5]:  # Show first 5 products only
                self.stdout.write(f'- {product.name}: ${product.price}')
            if products.count() > 5:
                self.stdout.write('  ... (more products not shown)')
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error checking products: {e}'))