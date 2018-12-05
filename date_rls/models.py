from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    genre = models.CharField(max_length=400)
    url = models.URLField()
    poster = models.ImageField(upload_to='posters')
    usermovies = models.ManyToManyField(User,related_name='movies',blank=True)
    def __str__(self):
        return self.name
