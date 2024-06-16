from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models import (
    TextChoices,
    TextField,
    Model,
    CASCADE,
    OneToOneField,
)
from .validators import validate_national_code


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


class Teacher(Model):
    user = OneToOneField(CustomUser, verbose_name="کاربر", on_delete=CASCADE)
    national_code = TextField(
        verbose_name="کدملی", max_length=15, validators=[validate_national_code]
    )
    license = TextField(verbose_name="کدپرسنلی", max_length=10)

    def clean(self):
        super().clean()
        if self.user.user_type != CustomUserType.TEACHER:
            raise ValidationError("نوع کاربر باید معلم تعریف شده باشد.")
