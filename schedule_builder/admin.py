from django.contrib import admin
from .models import Course
from .models import Blog
from django import forms

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Course)
admin.site.register(Blog, BlogAdmin)

