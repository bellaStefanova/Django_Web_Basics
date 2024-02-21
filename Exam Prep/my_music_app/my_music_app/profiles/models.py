from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.forms import ValidationError

def validate_username(value):
    for s in value:
        if not s.isalnum() and s not in ['_']:
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
        
# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=15,
                                validators=[MinLengthValidator(2), validate_username])
    
    email = models.EmailField()
    age = models.IntegerField(null=True, blank=True,
                              validators=[MinValueValidator(0)])