from django.db import models

# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length = 50)
	

class blogPost(models.Model):
        title = models.CharField(max_length=50)
        body = models.CharField(max_length=200)

