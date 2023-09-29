"""
WSGI config for tcs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tcs.settings')

application = get_wsgi_application()

# from whitenoise import WhiteNoise
# from .settings import STATIC_ROOT,MEDIA_ROOT
# # from tcs import MyWSGIApp

# # application = MyWSGIApp()
# application = WhiteNoise(application, root=STATIC_ROOT)
# application.add_files(MEDIA_ROOT)