from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    max_page = models.IntegerField(max_length=4)
    current_page = models.IntegerField(max_length=4)
