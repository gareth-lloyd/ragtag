import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'ragtag.settings_live'
os.environ['PYTHON_EGG_CACHE'] = '/var/www/.python-eggs'

sys.path.append('/var/www/django')
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

