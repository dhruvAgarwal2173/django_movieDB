from django.shortcuts import render
from .models import Movie
from .forms import MovieForm
from django.contrib import messages

# Create your views here.

def movie_add_view(request):
    form = MovieForm(request.POST)
    # print('\n\n********************')
    # print(form)
    if form.is_valid():
        form.save()
        # print('\n\n********************')
        # print(form)
    form = MovieForm
    form_context = {
        'movie' : form
        }
    messages.success(request, 'Movie has been added!')
    return render(request, 'movie/movie_add.html', form_context)


def movie_detail_view(request):
    movie = Movie.objects.all()
    movie_detail_context = {
        'movie': movie
    }
    return render(request, 'movie/movie_detail.html', movie_detail_context)

def movie_home_view(request):
    return render(request, 'movie/movie_home.html', {})
