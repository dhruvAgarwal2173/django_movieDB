from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm
from django.contrib import messages

# Create your views here.

def movie_add_view(request):
    form = MovieForm(request.POST)
    if form.is_valid():
        form.save()
    form = MovieForm
    context = {
        'movie' : form
        }
    messages.success(request, 'Movie has been added!')
    return render(request, 'movie/movie_add.html', context)


def movie_detail_view(request):
    movie = Movie.objects.all()
    context = {
        'movie': movie
    }
    return render(request, 'movie/movie_detail.html', context)

def movie_home_view(request):
    return render(request, 'movie/movie_home.html', {})

def movie_list_view(request):
    movie = Movie.objects.all()
    context = {
        'movie' : movie
    }
    return render(request, 'movie/movie_list.html', context)

