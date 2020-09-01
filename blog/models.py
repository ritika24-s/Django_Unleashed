from django.db import models
from django.core.urlresolvers import reverse
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

    def get_absolute_url(self):
        return reverse('blog_post_detail', kwargs={'year':self.pub_date.year,
                                                    'month':self.pub_date.month,
                                                    'slug':self.slug})
