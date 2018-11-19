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
logging.warning('test1')
if os.path.dirname(os.path.abspath(__file__)) == '/home/u/ug/ugradsa/usa-website/src/usa_website':
    activate_env=os.path.expanduser("~/usa-website/src/venv2/bin/activate_this.py")
    site.addsitedir('~/usa-website/src/venv2/lib/python2.7/site-packages')
    execfile(activate_env, dict(__file__=activate_env))
else:
    print(os.path.dirname(os.path.abspath(__file__)))
    activate_env=os.path.expanduser("./venv/Scripts/activate_this.py")
    site.addsitedir('./venv/lib/python3.6/site-packages')
    with open(activate_env) as f:
        exec(f.read(), {'__file__': activate_env})
#add external libs in venv
#site.addsitedir('/home/u/ug/ugradsa/usa-website/src/venv/lib/python2.7/site-packages')
#activate virtual env comment out the following two lines when local testing
#activate_env=os.path.expanduser("~/usa-website/src/venv/bin/activate_this.py")

#execfile(activate_env, dict(__file__=activate_env))
#exec(open(activate_env).read())

application = get_wsgi_application()
