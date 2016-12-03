from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from .models import Course

# Create your views here.
def index(request):
	courses = Course.objects.all()
	context = {"courses": courses}
	t = get_template("schedule_builder.html")
	vals = request.GET.getlist('course_name')
	html = t.render(context)
	return HttpResponse(html, context)

def home(request):
	html = get_template("index.html")
	context = Context({})
	return HttpResponse(html.render(context))

def aboutus(request):
	html = get_template("aboutus.html")
	context = Context({})
	return HttpResponse(html.render(context))

def stat133(request):
	t = get_template("stat-133.html")
	context = Context({})
	return HttpResponse(t.render(context))

def stat134(request):
	t = get_template("stat-134.html")
	context = Context({})
	return HttpResponse(t.render(context))

def stat135(request):
	t = get_template("stat-135.html")
	context = Context({})
	return HttpResponse(t.render(context))

def people(request):
	t = get_template("people.html")
	context = Context({})
	return HttpResponse(t.render(context))

def courseMap(request):
	t = get_template("course-map.html")
	context = Context({})
	return HttpResponse(t.render(context))

def project(request):
	t = get_template("project.html")
	context = Context({})
	return HttpResponse(t.render(context))
