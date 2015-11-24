
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from movie.models import Movie, Genre
from rest_framework import routers
from serializers import GenreSerializer,MovieSerializer
from permissions import IsNormalUser


######### ViewSets #########

class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated, IsNormalUser]
    queryset = Genre.objects.all()


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated, IsNormalUser]
    queryset = Movie.objects.all()


router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'genres', GenreViewSet)