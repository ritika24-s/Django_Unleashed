from django.db import models
from organizer.models import Startup, Tag
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63, unique_for_month='pub_date', help_text='A label for URL config')
    text = models.TextField()
    pub_date = models.DateField('date published', auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    startups = models.ManyToManyField(Startup, related_name='blog_posts')

    def __str__(self):
        return "{} on {}".format(self.title, self.pub_date.strfttime('%Y-%m-%d')) 
        # shows date time as datetime.date object

    class Meta:
        verbose_name = 'blog post'
        ordering = ['-pub_date','title']
        get_latest_by = 'pub_date'