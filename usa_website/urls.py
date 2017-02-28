"""usa_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import sys
import os
sys.path.append(os.path.abspath("~/usa-website/src/schedule_builder"))
import urls
from django.conf import settings
from django.conf.urls.static import static
from schedule_builder import views as extraViews
admin.autodiscover()

"""
urlpatterns = [
	url('^$', extraViews.home, name='home'),
	url('aboutus', extraViews.aboutus, name='aboutus'),
	url('index', extraViews.index, name='index'),
        url('stat-133', extraViews.stat133, name="stat133"),
        url('stat-134', extraViews.stat134, name="stat134"),
        url('stat-135', extraViews.stat135, name="stat135"),
        url('people', extraViews.people, name="people"),
        url('course-map', extraViews.courseMap, name="courseMap"),
        url('project', extraViews.project, name="project"),
	url(r'^schedule_builder/', include('schedule_builder.urls')),

"""
urlpatterns = [
        url('^', include('schedule_builder.urls')),
        url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
