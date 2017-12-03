from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length = 50)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    def __unicode__(self):
        return '%s' % self.title


    @models.permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

    def get_first_paragraph(self):
        return self.body.split("\n")[0]

