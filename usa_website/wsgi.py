"""
WSGI config for usa_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import site

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "usa_website.settings")
#add external libs in venv
site.addsitedir('/home/u/ug/ugradsa/usa-website/src/venv2/lib/python2.7/site-packages')
#activate virtual env
activate_env=os.path.expanduser("~/usa-website/src/venv2/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

application = get_wsgi_application()
