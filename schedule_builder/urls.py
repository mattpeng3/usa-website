from django.conf.urls import url
from schedule_builder import views

urlpatterns = [
	url(r'index$', views.index, name = 'index'),
	url(r'home$', views.home, name = 'home'),
	url(r'^$', views.home, name = 'home'),
	url(r'aboutus$', views.aboutus, name = 'aboutus'),
	url(r'stat-133$', views.stat133, name = "stat133"),
	url(r'stat-134$', views.stat134, name = "stat134"),
	url(r'stat-135$', views.stat135, name = "stat135"),
	#url(r'stat-150$', views.stat150, name = "stat150"),
	#url(r'stat-155$', views.stat155, name = "stat155"),
	url(r'people$', views.people, name = "people"),
	url(r'course-map$', views.courseMap, name = "courseMap"),
	url(r'project$', views.project, name = "project"),
        url(r'webdev$', views.webdev, name="webdev"),
        url(r'events$', views.events, name="events"),
        url(r'careerex$', views.careerex, name="careerex")
]
