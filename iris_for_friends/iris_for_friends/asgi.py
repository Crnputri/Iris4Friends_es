"""
Configuración ASGI para el proyecto iris_for_friends.

Expone el ASGI que puede llamarse como una variable de nivel módulo llamada ``application``.

Para más información acerca de este archivo, consulta
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anfisa_for_friends.settings')

application = get_asgi_application()
