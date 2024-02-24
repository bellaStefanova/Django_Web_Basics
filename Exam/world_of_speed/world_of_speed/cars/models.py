from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

from world_of_speed.profiles.models import Profile

class CarTypeChoices(models.TextChoices):

    RALLY = 'Rally', 'Rally'
    OPEN_WHEEL = 'Open-wheel', 'Open-wheel'
    KART = 'Kart', 'Kart'
    DRAG = 'Drag', 'Drag'
    OTHER = 'Other', 'Other'


class Car(models.Model):

    MAX_TYPE_LENGTH = 10

    MAX_MODEL_LENGTH = 15
    MIN_MODEL_LENGTH = 1

    MIN_YEAR_VALUE = 1999
    MAX_YEAR_VALUE = 2030

    MIN_PRICE_VALUE = 1


    type = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_TYPE_LENGTH,
        choices=CarTypeChoices.choices,
    )

    model = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_MODEL_LENGTH,
        validators=[
            MinLengthValidator(MIN_MODEL_LENGTH),
        ],
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(MIN_YEAR_VALUE, 'Year must be between 1999 and 2030!'),
            MaxValueValidator(MAX_YEAR_VALUE, 'Year must be between 1999 and 2030!'),
        ],
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        unique=True,
        error_messages={
            'unique': 'This image URL is already in use! Provide a new one.',
        },
        verbose_name='Image URL',
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(MIN_PRICE_VALUE),
        ],
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='cars',
    )

