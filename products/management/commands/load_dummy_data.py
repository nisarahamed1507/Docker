from django.core.management.base import BaseCommand
from django.utils.text import slugify
from products.models import Category, Product
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = 'Load dummy data into the database'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Product.objects.all().delete()
        Category.objects.all().delete()
        
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Created superuser admin/admin123'))
        
        # Create categories
        categories = [
            {'name': 'Electronics', 'slug': 'electronics'},
            {'name': 'Clothing', 'slug': 'clothing'},
            {'name': 'Books', 'slug': 'books'},
            {'name': 'Home & Kitchen', 'slug': 'home-kitchen'},
        ]
        
        category_objects = {}
        for cat in categories:
            category = Category.objects.create(name=cat['name'], slug=cat['slug'])
            category_objects[cat['name']] = category
            self.stdout.write(self.style.SUCCESS(f'Created category: {cat["name"]}'))
        
        # Create products
        products = [
            {
                'category': 'Electronics',
                'name': 'Smart TV 55 inch',
                'description': 'High-quality 4K smart TV with built-in streaming apps and voice control.',
                'price': 699.99,
            },
            {
                'category': 'Electronics',
                'name': 'Wireless Headphones',
                'description': 'Noise cancelling wireless headphones with 30 hour battery life.',
                'price': 149.99,
            },
            {
                'category': 'Electronics',
                'name': 'Smartphone',
                'description': 'Latest model smartphone with high-resolution camera and fast processor.',
                'price': 899.99,
            },
            {
                'category': 'Electronics',
                'name': 'Laptop',
                'description': 'Powerful laptop for work and entertainment with 16GB RAM and 512GB SSD.',
                'price': 1299.99,
            },
            {
                'category': 'Clothing',
                'name': 'T-Shirt',
                'description': 'Cotton t-shirt available in multiple colors.',
                'price': 19.99,
            },
            {
                'category': 'Clothing',
                'name': 'Jeans',
                'description': 'Classic fit jeans made from high quality denim.',
                'price': 49.99,
            },
            {
                'category': 'Clothing',
                'name': 'Hoodie',
                'description': 'Comfortable hoodie for casual wear, perfect for colder days.',
                'price': 39.99,
            },
            {
                'category': 'Books',
                'name': 'Python Programming Guide',
                'description': 'Comprehensive guide to Python programming for beginners and intermediate developers.',
                'price': 29.99,
            },
            {
                'category': 'Books',
                'name': 'Science Fiction Novel',
                'description': 'Award-winning science fiction novel set in a distant future.',
                'price': 14.99,
            },
            {
                'category': 'Home & Kitchen',
                'name': 'Coffee Maker',
                'description': 'Programmable coffee maker with multiple brewing options.',
                'price': 79.99,
            },
            {
                'category': 'Home & Kitchen',
                'name': 'Blender',
                'description': 'High-power blender for smoothies, soups, and more.',
                'price': 89.99,
            },
            {
                'category': 'Home & Kitchen',
                'name': 'Toaster Oven',
                'description': 'Versatile toaster oven for baking, toasting, and reheating.',
                'price': 69.99,
            },
        ]
        
        for product in products:
            Product.objects.create(
                category=category_objects[product['category']],
                name=product['name'],
                slug=slugify(product['name']),
                description=product['description'],
                price=product['price'],
                available=True
            )
            self.stdout.write(self.style.SUCCESS(f'Created product: {product["name"]}'))
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded dummy data'))