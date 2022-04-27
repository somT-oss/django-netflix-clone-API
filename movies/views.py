from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status 
from rest_framework.response import Response
from .serializers import MovieGenreSerializer, MoviesSerializer
from .models import MoviesGenre, Movies

@api_view(['GET'])
def movies_homepage(request):
    if request.method == 'GET':
        routes = {
            "all_movies": "movies/all-movies",
            "all_genre": "movies/all-genre",
            "type_of_movie": "movies/movie-type/<movie-genre>"
        }
        return Response({"ALL ENDPOINTS FOR MOVIES": routes}, status=status.HTTP_200_OK)

    else:
        return Response({"Error": "Invalid request type"})


@api_view(['GET'])
def all_movies(request):
    if request.method == 'GET':
        available_movies = Movies.objects.all()
        available_movies_serializer = MoviesSerializer(available_movies, many=True)

        return Response({"All Movies": available_movies_serializer.data}, status=status.HTTP_200_OK)

    else:
        return Response({"Error": "Invalid request type"})

@api_view(['GET'])
def all_genre(request):
    if request.method == 'GET':
        movie_genre = MoviesGenre.objects.all()
        movie_genre_serializer = MovieGenreSerializer(movie_genre, many=True)

        return Response({"All Genre": movie_genre_serializer.data}, status=status.HTTP_200_OK)
    
    else:
        return Response({"Error": "Invalid request type"})


@api_view(['GET'])
def type_of_movie(request, id):
    if request.method == 'GET':
        movie_based_on_genre = Movies.objects.get(movie_genre=id)
        movie_based_on_genre_serializer = MoviesSerializer(movie_based_on_genre)

        return Response({str(movie_based_on_genre.movie_genre): movie_based_on_genre_serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"Error": "Invalid request type"})