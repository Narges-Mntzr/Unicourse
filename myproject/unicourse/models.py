from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models import (
    TextChoices,
    TextField,
    Model,
    CASCADE,
    OneToOneField,
    CharField
)
from .validators import (
    validate_national_code,
    validate_phone_number
) 

class CustomUserType(TextChoices):
    TEACHER = ("teacher", "معلم")
    STUDENT = ("student", "دانشجو")
    INSTITUTE = ("institute", "آموزشگاه")


class CustomUser(AbstractUser):
    user_type = TextField(
        verbose_name="نوع کاربر",
        choices=CustomUserType.choices,
        default=CustomUserType.STUDENT,
        max_length=20,
    )
    phone_number = CharField(validators=[validate_phone_number], max_length=11)


class Teacher(Model):
    user = OneToOneField(CustomUser, verbose_name="User", on_delete=CASCADE)
    national_code = CharField(
        verbose_name="National Code", max_length=15, validators=[validate_national_code]
    )
    license = TextField(verbose_name="license", max_length=30)