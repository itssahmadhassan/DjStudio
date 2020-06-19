import datetime
from django.db import models



class Services(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    pic_url = models.URLField(max_length=200, default='', blank=True, null=True)
    upload_pic = models.ImageField(upload_to='static/images/', default='static/images/chiks.jpg', blank=True, null=True)
    upload_video = models.FileField(upload_to='static/videos/', default='', blank=True, null=True)
    pic_url = models.URLField(max_length=200, default='', blank=True, null=True)

    def __str__(self):
        return self.title


class About(models.Model):
    who_am_i = models.TextField(max_length=200)
    degree = models.SlugField(max_length=50)
    skills = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    x='About me'   # text shows when u click about in the admin section

    def __str__(self):
        return self.x

class Slider(models.Model):
    slider_pic_upload = models.ImageField(upload_to='static/slider_pics/', default='static/images/a2.jpg',)
    pic_url = models.URLField(max_length=200, default='', blank=True, null=True)


class Gallery(models.Model):
    upload_video = models.FileField(upload_to='static/videos/', default='', blank=True, null=True)
    upload_pic = models.ImageField(upload_to='static/gallery/', default='static/images/a2.jpg',)
    pic_url = models.URLField(max_length=200, default='', blank=True, null=True)
    caption = models.CharField(max_length=50, default='', blank=True, null=True)
