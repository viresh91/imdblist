from django.contrib.auth.models import Group
from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated, BasePermission
from movie.models import Movie, Genre
from rest_framework import routers

######### Permission Classes #########

class IsNormalUser(BasePermission):
    def has_permission(self, request, view):
        usergrp = Group.objects.get(name='user')
        if usergrp in request.user.groups.all() and request.method != 'GET':
            return False
        return True


######### Serializers #########

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('__all__')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('__all__')


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