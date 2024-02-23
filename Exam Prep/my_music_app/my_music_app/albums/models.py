from django.db import models
from django.core.validators import MinValueValidator
from my_music_app.profiles.models import Profile


class GenreChoices(models.TextChoices):
    POP = 'POP', 'Pop Music'
    JAZZ = 'JAZZ', 'Jazz Music'
    RNB = 'RNB', 'R&B Music'
    ROCK = 'ROCK', 'Rock Music'
    COUNTRY = 'COUNTRY', 'Country Music' 
    DANCE = 'DANCE', 'Dance Music'
    HIPHOP = 'HIPHOP', 'Hip Hop Music'
    OTHER = 'OTHER', 'Other'

class Album(models.Model):
    MAX_ALBUM_NAME_LENGTH = 30
    MAX_ARTIST_LENGTH = 30
    MAX_GENRE_LENGTH = 30
    MIN_PRICE_VALUE = 0


    album_name = models.CharField(
        max_length=MAX_ALBUM_NAME_LENGTH, 
        unique=True,
        verbose_name='Album Name',
    )

    artist = models.CharField(
        max_length=MAX_ARTIST_LENGTH,
    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH, 
        choices=GenreChoices.choices,
    )

    description = models.TextField(
        blank=True, 
        null=True,
    )

    image_url = models.URLField(
        verbose_name='Image URL',
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(MIN_PRICE_VALUE),
        ],
    )

    owner = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE, 
        related_name='albums',
    )