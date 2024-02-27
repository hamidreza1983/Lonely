"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.setting.production')
>>>>>>> a2f6af9 (api accounts complete serializer and url and making setting ok)

application = get_wsgi_application()
