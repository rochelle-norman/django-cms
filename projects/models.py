from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    featured_image = models.ImageField(blank=True)
    url = models.URLField()
    rank = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)
  
