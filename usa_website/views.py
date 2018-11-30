from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .models import Course, Blog
from django.views.generic import TemplateView
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from .forms import PostForm, AttendanceForm
from .utils.attendance import GetAttendanceHeader, GetAttendanceDetails, LookupSIDs
#from .utils.attendance import GetFinalTable



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

def index_new(request):
    html = get_template("index_new.html")
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

def officehours(request):
    html = get_template("officehours.html")
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
    t = get_template("course-map-old.html")
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

def education(request):
    t = get_template("education.html")
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
    t = get_template("blog/rp/a-shallow-dive-into-time-series-analysis-of-local-restaurant-data-using-r.html")
    context = Context({})
    return HttpResponse(t.render(context))

def tobacco_heart_disease(request):
    t = get_template("blog/rp/a-spatial-investigation-into-heart-disease-mortality-rates-and-youth-tobacco-rates.html")
    context = Context({})
    return HttpResponse(t.render(context))

def alphago(request):
    t = get_template("blog/rp/an-introduction-to-go-alphago-and-quantifying-go-gameplay.html")
    context = Context({})
    return HttpResponse(t.render(context))

def rapnet(request):
    t = get_template("blog/rp/rapnet-machine-learning-for-hip-hop-artist-classification.html")
    context = Context({})
    return HttpResponse(t.render(context))

def evol_lyrics(request):
    t = get_template("blog/rp/the-evolution-of-lyrics.html")
    context = Context({})
    return HttpResponse(t.render(context))

def ucb_ug_mental(request):
    t = get_template("blog/rp/uc-berkeley-undergraduates-general-mental-health-and-use-of-mental-health-services.html")
    context = Context({})
    return HttpResponse(t.render(context))

def world_happiness(request):
    t = get_template("blog/rp/world-happiness-report-eda.html")
    context = Context({})
    return HttpResponse(t.render(context))

def yelp_review(request):
    t = get_template("blog/rp/yelp-review-and-rating-analysis.html")
    context = Context({})
    return HttpResponse(t.render(context))

#######################################
###### WEB DEV TUTORIAL BLOG POSTS ######
#######################################

def website_tutorial_0(request):
    t = get_template("blog/education/website-tutorial-0.html")
    context = Context({})
    return HttpResponse(t.render(context))

def website_tutorial_1(request):
    t = get_template("blog/education/website-tutorial-1.html")
    context = Context({})
    return HttpResponse(t.render(context))

def website_tutorial_2(request):
    t = get_template("blog/education/website-tutorial-2.html")
    context = Context({})
    return HttpResponse(t.render(context))

def website_tutorial_3(request):
    t = get_template("blog/education/website-tutorial-3.html")
    context = Context({})
    return HttpResponse(t.render(context))


#####################################
###### SPRING 2018 DC PROJECTS ######
#####################################

def tutorfly(request):
    t = get_template("blog/dataconsulting/tutorfly.html")
    context = Context({})
    return HttpResponse(t.render(context))

def facial_emotion_recognition(request):
    t = get_template("blog/dataconsulting/facial-emotion-recognition.html")
    context = Context({})
    return HttpResponse(t.render(context))


def data_good(request):
    t = get_template("blog/dataconsulting/data-for-good-proposal.html")
    context = Context({})
    return HttpResponse(t.render(context))

#####################################
####### FALL 2017 DC PROJECTS #######
#####################################
def population_modeling(request):
    t = get_template("blog/dataconsulting/population-modeling.html")
    context = Context({})
    return HttpResponse(t.render(context))

def food_insecurity(request):
    t = get_template("blog/dataconsulting/food-insecurity.html")
    context = Context({})
    return HttpResponse(t.render(context))

###################################
########## CRASH COURSES ##########
###################################
def r0(request):
    t = get_template("blog/education/r0.html")
    context = Context({})
    return HttpResponse(t.render(context))

def r1(request):
    t = get_template("blog/education/r1.html")
    context = Context({})
    return HttpResponse(t.render(context))

def r2(request):
    t = get_template("blog/education/r2.html")
    context = Context({})
    return HttpResponse(t.render(context))

def p0(request):
    t = get_template("blog/education/p0.html")
    context = Context({})
    return HttpResponse(t.render(context))

def bias_variance(request):
    t = get_template("blog/education/bias-variance-decision-trees-ensemble-learning.html")
    context = Context({})
    return HttpResponse(t.render(context))

def ml_classification(request):
    t = get_template("blog/education/MLclassification.html")
    context = Context({})
    return HttpResponse(t.render(context))


###################################
######### MISCELLANEOUS ###########
###################################

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

#EASTEREGG
def housingcRincess(request):
    t = get_template("housingcRincess.html")
    context = Context({})
    return HttpResponse(t.render(context))

def aDishwasher(request):
    t = get_template("aDishwasher.html")
    context = Context({})
    return HttpResponse(t.render(context))

# def argentina(request):
#     t = get_template("webapp/Argentina.csv")
#     context = Context({})
#     return HttpResponse(t.render(context))

# def china(request):
#     t = get_template("webapp/china.csv")
#     context = Context({})
#     return HttpResponse(t.render(context))


# def guatemala(request):
#     t = get_template("webapp/Guatemala.csv")
#     context = Context({})
#     return HttpResponse(t.render(context))


# def nigeria(request):
#     t = get_template("webapp/Nigeria.csv")
#     context = Context({})
#     return HttpResponse(t.render(context))


# def sudan(request):
#     t = get_template("webapp/Sudan.csv")
#     context = Context({})
#     return HttpResponse(t.render(context))


# def unitedstates(request):
#     t = get_template("webapp/unitedstates.csv")
#     context = Context({})
#     return HttpResponse(t.render(context))


# def world(request):
#     t = get_template("webapp/world.csv")
#     context = Context({})
#     return HttpResponse(t.render(context))


# def benin(request):
#     t = get_template("webapp/Benin.csv")
#     context = Context({})
#     return HttpResponse(t.render(context))


# def tunisia(request):
#     t = get_template("webapp/Tunisia.csv")
#     context = Context({})
#     return HttpResponse(t.render(context))



# def user(request):
#     t = get_template("webapp/user.csv")
#     context = Context({})
#     return HttpResponse(t.render(context))

def housingcrisis(request):
    t = get_template("housingcrisis/index.html")
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
    t= get_template("webapp/convert_csv.py")
    context = Context({})
    return HttpResponse(t.render(context))

class AttendanceView(TemplateView):
    #Please view /usa_website/utils/attendance.py to understand GetAttendanceHeader + Details
    template_name = "attendance.html"

    def get(self, request):
        form = AttendanceForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AttendanceForm(request.POST)
        if form.is_valid():
            SID = form.cleaned_data['post']
            if SID == '0':
                text = "Error: Please Submit A Valid SID"
                form = AttendanceForm()
                args = {'form': form, 'text': text}
                return render(request, self.template_name, args)
            else:
                text = "Points Summary for SID - " + form.cleaned_data['post'] +":"
                values = LookupSIDs()
                head_list = GetAttendanceHeader(SID)
                det_list = GetAttendanceDetails(SID, values)
                if det_list == 1:
                    text = "Your SID does not appear in our records, please check if you have made an error or email us at 'contact@susa.berkeley'."
                    form = AttendanceForm()
                    args = {'form': form, 'text': text}
                    return render(request, self.template_name, args)
                form = AttendanceForm()
        else:
            text = "Error: Please Submit A Valid SID"

        args = {'form': form, 'text': text, 'head_list': head_list, 'det_list': det_list}
        return render(request, self.template_name, args)

#WEBDEV Fall 2018
def montyhall(request):
    t = get_template("montyhall.html")
    context = Context({})
    return HttpResponse(t.render(context))
