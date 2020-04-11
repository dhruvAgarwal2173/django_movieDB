from django.contrib import admin
from django.urls import path
from .views import movie_home_view, movie_add_view, movie_detail_view, movie_list_view

#app_name = 'movie'
urlpatterns = [
    path('', movie_home_view, name='movie-home'),
    path('add/', movie_add_view, name='movie-add'),
    path('detail/', movie_detail_view, name='movie-detail'),
    path('list/', movie_list_view, name='movie-list'),
]
