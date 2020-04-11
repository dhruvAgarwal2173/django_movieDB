from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=150, unique=True)
    genre = models.CharField(max_length=75, )
    release = models.CharField(max_length=4, help_text='Enter the initial release year')
    rating = models.CharField(max_length=1,help_text="Enter a value from 1 to 10")
    #image = models.ImageField()
    def __str__(self):
        return self.title