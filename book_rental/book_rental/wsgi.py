"""
WSGI config for book_rental project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_rental.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root="/usr/src/book_rental/staticfilestorun")
#application.add_files("/path/to/more/static/files", prefix="more-files/")