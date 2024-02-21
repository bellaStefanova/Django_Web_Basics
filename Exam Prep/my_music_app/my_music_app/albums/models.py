from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Album(models.Model):
    GENRE_CHOICES = (
        ('POP', 'Pop Music'),
        ('JAZZ', 'Jazz Music'),
        ('R&B', 'R&B Music'),
        ('ROCK', 'Rock Music'),
        ('COUNTRY', 'Country Music'),
        ('DANCE', "Dance Music"),
        ('HIPHOP', 'Hip Hop Music'),
        ('OTHER', 'Other'),
    )

    album_name = models.CharField(max_length=30, unique=True)
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField()
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    owner = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='albums')