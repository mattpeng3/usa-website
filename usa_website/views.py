from django.http import HttpResponse

from django.template.loader import get_template
from django.template import Context
from .models import Course, Blog
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from .forms import PostForm



# Create your views here.
def index(request):
        #return render(request, 'schedule_builder.html', {})
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
    return HttpResponse(html.render({}))

def calendar(request):
    html = get_template("calendar.html")
    context = Context({})
    return HttpResponse(html.render({}))

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

def stat150(request):
    t = get_template("stat-150.html")
    context = Context({})
    return HttpResponse(t.render(context))

def stat151a(request):
    t = get_template("stat-151a.html")
    context = Context({})
    return HttpResponse(t.render(context))

def stat151b(request):
    t = get_template("stat-151b.html")
    context = Context({})
    return HttpResponse(t.render(context))

def stat152(request):
    t = get_template("stat-152.html")
    context = Context({})
    return HttpResponse(t.render(context))

def stat153(request):
    t = get_template("stat-153.html")
    context = Context({})
    return HttpResponse(t.render(context))

def stat154(request):
    t = get_template("stat-154.html")
    context = Context({})
    return HttpResponse(t.render(context))

def stat155(request):
    t = get_template("stat-155.html")
    context = Context({})
    return HttpResponse(t.render(context))

def stat157(request):
    t = get_template("stat-157.html")
    context = Context({})
    return HttpResponse(t.render(context))

def stat158(request):
    t = get_template("stat-158.html")
    context = Context({})
    return HttpResponse(t.render(context))

def stat159(request):
    t = get_template("stat-159.html")
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


def webdev(request):
    t = get_template("webdev.html")
    context = Context({})
    return HttpResponse(t.render(context))

def careerex(request):
    t = get_template("careerex.html")
    context = Context({})
    return HttpResponse(t.render(context))

def research(request):
    t = get_template("research.html")
    context = Context({})
    return HttpResponse(t.render(context))
def dataconsulting(request):
    t = get_template("dataconsulting.html")
    context = Context({})
    return HttpResponse(t.render(context))
def comingSoon(request):
    t = get_template("comingSoon.html")
    context = Context({})
    return HttpResponse(t.render(context))

def yitz(request):
    t = get_template("yitz.html")
    context = Context({})
    return HttpResponse(t.render(context))

def blog(request):
    return render_to_response('blog/blog.html', {
        'posts': Blog.objects.all()#[-1:-6:-1]
    })

    #t = get_template("blog/blog.html")
    #context = Context({})
    #return HttpResponse(t.render(context))

##################################
###### FALL 2017 BLOG POSTS ######
##################################

def shallow_dive(request):
    t = get_template("blog/a-shallow-dive-into-time-series-analysis-of-local-restaurant-data-using-r.html")
    context = Context({})
    return HttpResponse(t.render(context))

def tobacco_heart_disease(request):
    t = get_template("blog/a-spatial-investigation-into-heart-disease-mortality-rates-and-youth-tobacco-rates.html")
    context = Context({})
    return HttpResponse(t.render(context))

def alphago(request):
    t = get_template("blog/an-introduction-to-go-alphago-and-quantifying-go-gameplay.html")
    context = Context({})
    return HttpResponse(t.render(context))

def rapnet(request):
    t = get_template("blog/rapnet-machine-learning-for-hip-hop-artist-classification.html")
    context = Context({})
    return HttpResponse(t.render(context))

def evol_lyrics(request):
    t = get_template("blog/the-evolution-of-lyrics.html")
    context = Context({})
    return HttpResponse(t.render(context))

def ucb_ug_mental(request):
    t = get_template("blog/uc-berkeley-undergraduates-general-mental-health-and-use-of-mental-health-services.html")
    context = Context({})
    return HttpResponse(t.render(context))

def world_happiness(request):
    t = get_template("blog/world-happiness-report-eda.html")
    context = Context({})
    return HttpResponse(t.render(context))

def yelp_review(request):
    t = get_template("blog/yelp-review-and-rating-analysis.html")
    context = Context({})
    return HttpResponse(t.render(context))

##################################



def view_post(request, slug):
    return render_to_response('viewPost.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_author(request, author):
    return render_to_response('viewAuthor.html', {
        'posts': Blog.objects.all()
    })

def susawebapp(request):
    t = get_template("webapp/index.html")
    context = Context({})
    return HttpResponse(t.render(context))

def argentina(request):
    t = get_template("SUSA-web-app/Argentina.csv")
    context = Context({})
    return HttpResponse(t.render(context))

def china(request):
    t = get_template("SUSA-web-app/china.csv")
    context = Context({})
    return HttpResponse(t.render(context))


def guatemala(request):
    t = get_template("SUSA-web-app/Guatemala.csv")
    context = Context({})
    return HttpResponse(t.render(context))


def nigeria(request):
    t = get_template("SUSA-web-app/Nigeria.csv")
    context = Context({})
    return HttpResponse(t.render(context))


def sudan(request):
    t = get_template("SUSA-web-app/Sudan.csv")
    context = Context({})
    return HttpResponse(t.render(context))


def unitedstates(request):
    t = get_template("SUSA-web-app/unitedstates.csv")
    context = Context({})
    return HttpResponse(t.render(context))


def world(request):
    t = get_template("SUSA-web-app/world.csv")
    context = Context({})
    return HttpResponse(t.render(context))


def benin(request):
    t = get_template("SUSA-web-app/benin.csv")
    context = Context({})
    return HttpResponse(t.render(context))


def tunisia(request):
    t = get_template("SUSA-web-app/Tunisia.csv")
    context = Context({})
    return HttpResponse(t.render(context))



def user(request):
    t = get_template("SUSA-web-app/user.csv")
    context = Context({})
    return HttpResponse(t.render(context))

def textboxio(request):
    t = get_template("textboxio/textboxio.js")
    context = Context({})
    return HttpResponse(t.render(context))


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = "-".join(post.title.split(" "))
            post.save()
            return redirect('/blog/view/' + post.slug + ".html")
    else: 
        form = PostForm()

    return render(request, 'submit.html', {'form': form})

def convert_csv(request):
    t= get_template("SUSA-web-app/convert_csv.py")
    context = Context({})
    return HttpResponse(t.render(context))

