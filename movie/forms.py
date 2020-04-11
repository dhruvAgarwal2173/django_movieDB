#from django.forms import ModelForm
from django import forms
from .models import Movie
from django import forms

class MovieForm(forms.ModelForm):
    # title = forms.CharField(label='Title')
    # genre = forms.CharField(label='Genre')
    # release = forms.CharField(label='Release year', help_text="Enter in MM-YYYY format")
    # rating = forms.CharField(label='Rating', help_text="Enter the rating on a scale of 1-10")

    class Meta:
        model = Movie
        fields = [
            'title',
            'genre',
            'release',
            'rating',
        ]
