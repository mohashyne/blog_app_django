from django.db import models
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)

# This will display the title of the article in the admin panel instead of the default 'Article object'
# This is a dunder method which is called when you try to print the object, it returns the title of the article and not the object, something like stringify the object.

    def __str__(self):
        return str(self.title)

    def snippet(self):
        return str(self.body)[:50] + '...'

    # This will return the absolute url of the article
    # by calling this in our template, we can get the url of the article
    # <!-- <h2><a href="{{ article.get_absolute_url }}">{{ article.title }}</a></h2> -->
    def get_absolute_url(self):
        return reverse('article_detail', args=[self.slug])


# NOTE: After creating the model, you need to create a migration file and apply it to the database
# python manage.py makemigrations # this will create the migration file
# python manage.py migrate # this will apply the migration file to the database
