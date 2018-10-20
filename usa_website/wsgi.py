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

if __file__ == '/home/u/ug/ugradsa/usa-website/src/usa_website/wsgi.py':
    activate_env=os.path.expanduser("/home/u/ug/ugradsa/usa-website/src/venv/bin/activate_this.py")
    site.addsitedir('/home/u/ug/ugradsa/usa-website/src/venv/lib/python3.4/site-packages')
    print(activate_env)
    #execfile(activate_env, dict(__file__=activate_env))
    execfile(activate_env, dict(__file__=activate_env))
else:
    activate_env=os.path.expanduser("./venv/bin/activate_this.py")
    site.addsitedir('./venv/lib/python3.6/site-packages')
    print(activate_env)
    with open(activate_env) as f:
        exec(f.read(), {'__file__': activate_env})
#add external libs in venv
#site.addsitedir('/home/u/ug/ugradsa/usa-website/src/venv/lib/python2.7/site-packages')
#activate virtual env comment out the following two lines when local testing
#activate_env=os.path.expanduser("~/usa-website/src/venv/bin/activate_this.py")

#execfile(activate_env, dict(__file__=activate_env))
#exec(open(activate_env).read())

application = get_wsgi_application()
