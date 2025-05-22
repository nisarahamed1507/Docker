import os

# ...existing code...

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Ensure this points to the 'media' folder

# ...existing code...