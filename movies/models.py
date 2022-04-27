from django.db import models


class MoviesGenre(models.Model):
    category = (
        ('Horror', 'Horror'),
        ('Comedy', 'Comedy'),
        ('Anime', 'Anime'),
        ('Romantic Comedy', 'Romantic Comedy'),
        ('Action', 'Action'),
        ('Drama', 'Drama')
    )

    all_genre = models.CharField(choices=category, max_length=90)

    def __str__(self):
        return self.all_genre


class Movies(models.Model):
    movie_name = models.CharField(max_length=244)
    movie_description = models.CharField(max_length=500)
    movie_art = models.ImageField(null=True)
    movie_genre = models.ForeignKey(MoviesGenre, on_delete=models.CASCADE)
    


    def __str__(self):
        return self.movie_name