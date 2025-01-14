from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

# This will display the title of the article in the admin panel instead of the default 'Article object'
# This is a dunder method which is called when you try to print the object, it returns the title of the article and not the object, something like stringify the object.

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'


# TODO: add thumbnail later and add author

# NOTE: After creating the model, you need to create a migration file and apply it to the database
# python manage.py makemigrations # this will create the migration file
# python manage.py migrate # this will apply the migration file to the database
