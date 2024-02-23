from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from my_music_app.helpers.model_validators import validate_username


class Profile(models.Model):
    MIN_USERNAME_LENGTH = 2
    MAX_USERNAME_LENGTH = 15

    MIN_AGE_VALUE = 0


    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=[
            MinLengthValidator(MIN_USERNAME_LENGTH), 
            validate_username,
        ],
    )

    email = models.EmailField(
    )

    age = models.IntegerField(
        null=True, 
        blank=True,
        validators=[
            MinValueValidator(MIN_AGE_VALUE),
        ],
    )