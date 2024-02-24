from django.forms import ValidationError


def validate_username(value):
    for s in value:
        if not (s.isalnum() or s == '_'):
            raise ValidationError("Username must contain only letters, digits, and underscores!")