from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.CharField(max_length=100)
    genre = models.CharField(choices=Genre.choices, max_length=5)
    biography = models.CharField(max_length=1000)
    year_formed = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2100)]
    )
    active = models.BooleanField(default=True)
    official_homepage = models.URLField(null=True, blank=True)
    like_new = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Listing(models.Model):
    class Type(models.TextChoices):
        RECORDS = 'RE',
        CLOTHING = 'CL',
        POSTERS = 'PO',
        MISCELLANEOUS = 'MI',

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    sold = models.BooleanField(default=False)
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2100)], null=True, blank=True)
    type = models.CharField(max_length=2, choices=Type.choices)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
