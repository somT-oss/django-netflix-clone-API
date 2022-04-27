from unicodedata import name
from django.urls import path 
from . import views 

urlpatterns = [
    path("home/", views.movies_homepage, name='movies-homepage'),
    path("all-movies/", views.all_movies, name='all-movies'),
    path("all-genre/", views.all_genre, name='all-genre'),
    path("genre-type/<int:id>/", views.type_of_movie, name="genre-type")
]