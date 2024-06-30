from django.contrib import admin
from django.urls import include, path
from .views import *
from django.contrib.sitemaps.views import sitemap 
from blog.sitemap import BlogModelSitemap 
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('',home, name="home"),
    path('blog_detail/<slug>',blog_detail, name="blog_detail"),
    path('about',about_view, name="about_view"),
    path('contact',contact_view, name="contact_url"),
    path('search',SearchView.as_view(), name="search"),
    path('sitemap.xml', sitemap, {'sitemaps': {'blogmodel' : BlogModelSitemap}}, 
     name='django.contrib.sitemaps.views.sitemap') ,
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('blog/img/favicon.ico')))



]
