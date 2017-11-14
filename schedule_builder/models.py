from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length = 50)

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    #author = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    summary = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.title


    @models.permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })


class William(models.Model):
    title = models.CharField(max_length=100, unique=True)

