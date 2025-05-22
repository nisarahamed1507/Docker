from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ...existing code...
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)