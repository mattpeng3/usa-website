"""
WSGI config for usa_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import site
import logging

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "usa_website.settings")

if os.path.dirname(os.path.abspath(__file__)) == '/home/u/ug/ugradsa/usa-website/src/usa_website':
    activate_env=os.path.expanduser("~/usa-website/src/venv2/bin/activate_this.py")
    site.addsitedir('~/usa-website/src/venv2/lib/python2.7/site-packages')
    execfile(activate_env, dict(__file__=activate_env))
elif os.path.isdir(os.path.abspath(os.path.join(os.pardir,'venv/Scripts'))):
    activate_env=os.path.expanduser("./venv/Scripts/activate_this.py")
    site.addsitedir('./venv/lib/python3.6/site-packages')
    with open(activate_env) as f:
        exec(f.read(), {'__file__': activate_env})
else:
    activate_env=os.path.expanduser("./venv/bin/activate_this.py")
    site.addsitedir('./venv/lib/python3.6/site-packages')
    with open(activate_env) as f:
        exec(f.read(), {'__file__': activate_env})


application = get_wsgi_application()
