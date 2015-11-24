__author__ = 'viresh'
from rest_framework import viewsets, serializers
from movie.models import Movie, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('__all__')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('__all__')

