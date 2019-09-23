from django.db import models
from django.db.models import permalink
from tinymce.models import HTMLField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return 'view_blog_category', None, {'slug': self.slug}


class Blog(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    slug = models.SlugField(max_length=500)
    caption = models.CharField(max_length=500)
    image_upload = models.ImageField(upload_to='hindi/media')
    article = models.TextField()
    video = models.CharField(null=True, blank=True,max_length=700)
    articlemain = models.TextField(null=True, blank=True)
    embed = models.CharField(null=True, blank=True,max_length=1000)
    time = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __unicode__(self):
        return 'Blog : ' + self.caption

    def __str__(self):
        return 'Blog : ' + self.caption

    @permalink
    def get_absolute_url(self):
        return 'view_blog_post', None, {'slug': self.slug}


class Epaper(models.Model):
    e_paper_name = models.CharField(max_length=50)
    e_paper = models.FileField(upload_to='hindi/Epaper')
    date = models.DateField()

    def __unicode__(self):
        return 'Epaper : ' + self.e_paper_name

    def __str__(self):
        return 'Epaper : ' + self.e_paper_name


class Trailer(models.Model):
    trailer_name = models.CharField(max_length=50)
    trailer_url = models.TextField()

    def __unicode__(self):
        return 'Tralier : ' + self.trailer_name

    def __str__(self):
        return 'Tralier : ' + self.trailer_name
