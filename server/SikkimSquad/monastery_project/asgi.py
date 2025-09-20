"""
ASGI config for monastery_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monastery_project.settings')

application = get_asgi_application()
