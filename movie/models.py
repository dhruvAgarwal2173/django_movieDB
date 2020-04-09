from django.db import models
from django.utils import timezone

# Create your models here.

class movie_add(models.Model):
    title = models.CharField(unique=True, blank=False, null=False, help_text='Please enter the movie name', max_length=250)
    genre = models.CharField(max_length=10, choices=[
        ('AC', 'Action'),
        ('CO', 'Comedy'),
        ('TH', 'Thriller'),
        ('SH', 'Shit'),
    ])
    date_release = models.DateField(unique=False, help_text='Enter date of movie release')
    date_added = models.DateTimeField(default=timezone.now, help_text='Enter date of addition to database')


#
# class movie_delete():
#     pass
#
# class movie_list():
#     pass
#
# class movie_detail():
#     pass