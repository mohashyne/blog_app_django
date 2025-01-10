from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
 

# TODO: add thumbnail later and add author  

# NOTE: After creating the model, you need to create a migration file and apply it to the database  
# python manage.py makemigrations # this will create the migration file
# python manage.py migrate # this will apply the migration file to the database