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
	url(r'project$', views.project, name = "project"),
        url(r'webdev$', views.webdev, name="webdev"),
        url(r'research$', views.research, name="research"),
        url(r'careerex$', views.careerex, name="careerex")
]
