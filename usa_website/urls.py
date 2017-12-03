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
sys.path.insert(0, 'schedule_builder')
sys.path.insert(1, '../schedule_builder')
#import urls
from django.conf import settings
from django.conf.urls.static import static
#from schedule_builder import views as extraViews
from usa_website import views
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
        url(r'^admin/', admin.site.urls),
    url(r'index$', views.index, name = 'index'),
    url(r'home$', views.home, name = 'home'),
    url(r'^$', views.home, name = 'home'),
    url(r'aboutus$', views.aboutus, name = 'aboutus'),
    url(r'calendar$', views.calendar, name = 'calendar'),
    url(r'stat-133$', views.stat133, name = "stat133"),
    url(r'stat-134$', views.stat134, name = "stat134"),
    url(r'stat-135$', views.stat135, name = "stat135"),
    url(r'stat-150$', views.stat150, name = "stat150"),
    url(r'stat-151a$', views.stat151a, name = "stat151a"),
    url(r'stat-151b$', views.stat151b, name = "stat151b"),
    url(r'stat-152$', views.stat152, name = "stat152"),
    url(r'stat-153$', views.stat153, name = "stat153"),
    url(r'stat-154$', views.stat154, name = "stat154"),
    url(r'stat-155$', views.stat155, name = "stat155"),
    url(r'stat-157$', views.stat157, name = "stat157"),
    url(r'stat-158$', views.stat158, name = "stat158"),
    url(r'stat-159$', views.stat159, name = "stat159"),
    url(r'people$', views.people, name = "people"),
    url(r'course-map$', views.courseMap, name = "courseMap"),
    url(r'dataconsulting$', views.dataconsulting, name = "dataconsulting"),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'webdev$', views.webdev, name="webdev"),
    url(r'careerex$', views.careerex, name="careerex"),
    url(r'research$', views.research, name="research"),
    url(r'comingSoon$', views.comingSoon, name="comingSoon"),
    url(r'blog$', views.blog, name="blog"),
    url(r'textboxio/textboxio.js', views.textboxio, name = "textboxio"),
    url(r'yitz$', views.yitz, name = "yitz"),
    url(r'^blog/view/(?P<slug>[^\.]+).html', views.view_post, name='view_blog_post'),
    url(r'webapp/', views.susawebapp, name = "susawebapp"),
    url(r'webapp/Argentina.csv', views.argentina, name = "argentina"),
    url(r'webapp/china.csv', views.china, name = "china"),
    url(r'webapp/Guatemala.csv', views.guatemala, name = "guatemala"),
    url(r'webapp/Nigeria.csv', views.nigeria, name = "nigeria"),
    url(r'webapp/Sudan.csv', views.sudan, name = "sudan"),
    url(r'webapp/unitedstates.csv', views.unitedstates, name = "unitedstates"),
    url(r'webapp/world.csv', views.world, name = "world"),
    url(r'webapp/Benin.csv', views.benin, name = "benin"),
    url(r'webapp/Tunisia.csv', views.tunisia, name = "tunisia"),
    url(r'webapp/user.csv', views.user, name = "user"),
    url(r'webapp/convert_csv.py', views.convert_csv, name = "convert_csv"),
    url(r'Argentina.csv', views.argentina, name = "argentina"),
    url(r'china.csv', views.china, name = "china"),
    url(r'Guatemala.csv', views.guatemala, name = "guatemala"),
    url(r'Nigeria.csv', views.nigeria, name = "nigeria"),
    url(r'Sudan.csv', views.sudan, name = "sudan"),
    url(r'unitedstates.csv', views.unitedstates, name = "unitedstates"),
    url(r'world.csv', views.world, name = "world"),
    url(r'Benin.csv', views.benin, name = "benin"),
    url(r'Tunisia.csv', views.tunisia, name = "tunisia"),
    url(r'user.csv', views.user, name = "user"),
    url(r'convert_csv.py', views.convert_csv, name = "convert_csv"),
    url(r'yitz/textboxio/textboxio.js', views.textboxio, name = "textboxio")
        #url('^', include('schedule_builder.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
