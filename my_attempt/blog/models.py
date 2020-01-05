from django.db import models

# Create your models here.

class BlogPost(models.Model):
    
    slug = models.SlugField(unique = True)
    Title = models.CharField(null = False, max_length = 100)
    Content = models.TextField(null=False, blank=False)
    Sender = models.CharField(null = False, max_length = 100)


