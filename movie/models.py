from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=30)
    imdb_score = models.FloatField()
    genre = models.ManyToManyField(to=Genre)

    def __unicode__(self):
        return u'%s' % self.name


