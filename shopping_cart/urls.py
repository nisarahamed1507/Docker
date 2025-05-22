from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products.views import home
from cart.views import checkout, order_complete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('users/', include('users.urls')),
    path('checkout/', checkout, name='checkout'),
    path('order-complete/', order_complete, name='order_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)