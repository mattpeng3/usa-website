from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from .models import Course

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
