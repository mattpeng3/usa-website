from django.db import models

# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length = 50)
	

class Blog(models.Model):
        title = models.CharField(max_length=100, unique=True)
        slug = models.SlugField(max_length=100, unique=True)
        body =models.TextField()
        posted = models.DateField(db_index=100, unique=True)
        category = models.ForeignKey('blog.Category')

class Category(models.Model):
        title = models.CharField(max_length=100, db_index=True)
        slug = models.SlugField(max_length=100, db_index=True)

