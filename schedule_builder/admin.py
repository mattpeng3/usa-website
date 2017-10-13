from django.contrib import admin
from .models import Course
from .models import blogPost
from .models import Blog
from django import forms

# Register your models here.
admin.site.register(Course)
admin.site.register(blogPost)
admin.site.register(Blog)
