from django.core.exceptions import ValidationError
import re


def validate_national_code(value):
    if not re.match(r"^\d{10}$", value):
        raise ValidationError("کدملی باید ۱۰ رقم باشد.")

def validate_phone_number(value):
    if len(value) != 11:
        raise ValidationError("شماره همراه باید ۱۱ رقم باشد.")
    if not value.startswith('09'):
        raise ValidationError("شماره همراه وارد شده معتبر نیست.")
