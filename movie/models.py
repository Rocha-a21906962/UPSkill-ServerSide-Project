from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from actor.models import Actor
from director.models import Director


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        pass


class Movie(models.Model):
    SCORE = [(i, i) for i in range(11)]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    year = models.PositiveSmallIntegerField(validators=[MaxValueValidator(2500), MinValueValidator(1895)])
    genres = models.ManyToManyField(Genre, blank=True)
    image = models.ImageField(upload_to="movie/%Y/%m/%d/", blank=True)
    rating = models.IntegerField(default=0, choices=SCORE)
    actors = models.ManyToManyField(Actor, blank=True)
    directors = models.ManyToManyField(Director, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        pass
