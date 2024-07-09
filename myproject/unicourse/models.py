from django.contrib.auth.models import AbstractUser
from django.db.models import (
    TextChoices,
    TextField,
    Model,
    CASCADE,
    OneToOneField,
    CharField,
    BooleanField,
    DateField,
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
    address = TextField(verbose_name="Address", max_length=200)
    license = TextField(verbose_name="License", max_length=30)
    is_approved = BooleanField(verbose_name="Is Approved", default=False)


class SchoolTypeChoices(TextChoices):
    HIGH_SCHOOL = ("high", "دبیرستان")
    MIDDLE_SCHOOL = ("middle", "راهنمایی")
    ELEMENTARY_SCHOOL = ("elementary", "دبستان")


class Student(Model):
    user = OneToOneField(CustomUser, verbose_name="User", on_delete=CASCADE)
    birthday = DateField(verbose_name="تاریخ تولد")
    school = TextField(max_length=30, verbose_name="اسم مدرسه")
    type_of_school = TextField(
        verbose_name="مقطع تحصیلی",
        choices=SchoolTypeChoices.choices,
        default=SchoolTypeChoices.ELEMENTARY_SCHOOL,
        max_length=20,
    )

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
