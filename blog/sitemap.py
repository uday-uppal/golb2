from django.contrib.sitemaps import Sitemap 
from .models import BlogModel 
  
class BlogModelSitemap(Sitemap): 
    protocol = 'https'
    def items(self): 
        return BlogModel.objects.all().order_by('-created_at') 
        
    def lastmod(self, obj): 
        return obj.upload_to
