from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

from world_of_speed.helpers.model_validators import validate_username

class Profile(models.Model):

    MIN_USERNAME_LENGTH = 3
    MAX_USERNAME_LENGTH = 15

    MIN_AGE_VALUE = 21

    MAX_PASSWORD_LENGTH = 20

    MAX_FIRST_NAME_LENGTH = 25

    MAX_LAST_NAME_LENGTH = 25


    username = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_USERNAME_LENGTH,
        validators=[
            MinLengthValidator(MIN_USERNAME_LENGTH, 'Username must be at least 3 chars long!'), 
            validate_username,
        ],
    )

    email = models.EmailField(
        null=False,
        blank=False,
        max_length=100,
    )

    age = models.IntegerField(
        null=False, 
        blank=False,
        validators=[
            MinValueValidator(MIN_AGE_VALUE),
        ],
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_PASSWORD_LENGTH,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_FIRST_NAME_LENGTH,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LAST_NAME_LENGTH,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture',
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
