from rest_framework import serializers
from .models import Movies, MoviesGenre

class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies 
        fields = '__all__'


class MovieGenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = MoviesGenre
        fields = ['all_genre']

    
