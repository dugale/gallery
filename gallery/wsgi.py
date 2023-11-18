"""
WSGI config for gallery project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
import os
#def application(environ, start_response):
#    if environ['mod_wsgi.process_group'] != '': 
#        import signal
#        os.kill(os.getpid(), signal.SIGINT)
#    return ["killed"]
import sys
sys.path.append("/home/bitnami/.local/lib/python3.8/site-packages")

from django.core.wsgi import get_wsgi_application
from PIL import Image

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gallery.settings')

application = get_wsgi_application()
