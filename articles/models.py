from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    body = models.TextField
    date = models.DateTimeField(auto_now_add=True)
 

# TODO: add thumbnail later and add author  