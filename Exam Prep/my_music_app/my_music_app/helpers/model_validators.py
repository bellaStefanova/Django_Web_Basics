from django.forms import ValidationError


def validate_username(value):
    for s in value:
        if not (s.isalnum() or s == '_'):
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")