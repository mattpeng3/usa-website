from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. Welcome to the schedule building page.")

# Create your views here.
