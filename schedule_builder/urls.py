from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'home', views.home, name = 'home'),
	url(r'aboutus', views.aboutus, name = 'aboutus'),
	url(r'stat-133', views.stat133, name = "stat133"),
	url(r'stat-134', views.stat134, name = "stat134"),
	url(r'stat-135', views.stat135, name = "stat135"),
	url(r'people', views.people, name = "people"),
	url(r'course-map', views.courseMap, name = "courseMap"),
	url(r'project', views.project, name = "project")
]