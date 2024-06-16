from django.core.exceptions import ValidationError
import re


def validate_national_code(value):
    if not re.match(r"^\d{10}$", value):
        raise ValidationError("کدملی باید ۱۰ رقم باشد.")
