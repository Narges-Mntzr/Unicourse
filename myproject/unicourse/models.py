from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models import (
    TextChoices,
    TextField,
    Model,
    CASCADE,
    OneToOneField,
    CharField,
    BooleanField,
)
from .validators import validate_national_code, validate_phone_number


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


class Institute(Model):
    user = OneToOneField(CustomUser, verbose_name="User", on_delete=CASCADE)
    name = CharField(verbose_name="Institute Name", max_length=100, unique=True)
    address = TextField(verbose_name="Address", max_length=200)
    license = TextField(verbose_name="License", max_length=30)
    is_approved = BooleanField(verbose_name="Is Approved", default=False)
