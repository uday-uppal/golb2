from distutils.command.upload import upload
from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from .hh import generate_slug
from django.urls import reverse

class BlogModel(models.Model):
    title=models.CharField(max_length=1000)
    content=models.CharField(max_length=10000000)
    slug=models.SlugField(max_length=1000, null=True, blank=True)
    image=models.ImageField(upload_to="blog")
    created_at=models.DateTimeField(auto_now_add=True)
    upload_to=models.DateTimeField(auto_now=True)
    author=models.CharField(max_length=1000,default="Purple Penguin")
    read_time=models.IntegerField(default=5)
    def __str__(self):
        return self.title
    def save(self, *args,**kwargs):
        self.slug=generate_slug(self.title)
        super(BlogModel,self).save(*args,**kwargs)
    def get_absolute_url(self): 
        return reverse('blog_detail',kwargs={'slug': self.slug})    
class contact_model(models.Model):
    email=models.EmailField()       
    subject=models.CharField(max_length=1000)
    message=models.CharField(max_length=1000)
    def __str__(self):
        return self.email 
