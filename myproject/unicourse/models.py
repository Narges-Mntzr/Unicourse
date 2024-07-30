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
    ForeignKey,
    IntegerField,
    JSONField,
    TimeField,
    URLField,
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

    def __str__(self) -> str:
        return self.first_name


class Teacher(Model):
    user = OneToOneField(CustomUser, verbose_name="User", on_delete=CASCADE)
    national_code = CharField(
        verbose_name="National Code", max_length=15, validators=[validate_national_code]
    )
    license = TextField(verbose_name="license", max_length=30)

    def __str__(self) -> str:
        return self.user.first_name


class Institute(Model):
    user = OneToOneField(CustomUser, verbose_name="User", on_delete=CASCADE)
    address = TextField(verbose_name="Address", max_length=200)
    license = TextField(verbose_name="License", max_length=30)
    is_approved = BooleanField(verbose_name="Is Approved", default=False)

    def __str__(self) -> str:
        return self.user.first_name


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

    def __str__(self) -> str:
        return self.user.first_name

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"


class Course(Model):
    institute = ForeignKey(verbose_name="آموزشگاه", to=Institute, on_delete=CASCADE)
    teacher = ForeignKey(verbose_name="استاد", to=Teacher, on_delete=CASCADE)
    name = TextField(max_length=30, verbose_name="اسم دوره")
    price = IntegerField(verbose_name="هزینه دوره", default=0)
    prerequisite = JSONField(verbose_name="دوره های پیشنیاز", default=list, blank=True)
    start_date = DateField(verbose_name="تاریخ شروع دوره")
    end_date = DateField(verbose_name="تاریخ پایان دوره")
    days_of_week = JSONField(verbose_name="روزهای برگزاری دوره در هفته", default=list)
    class_start_time = TimeField(verbose_name="زمان شروع دوره در روز")
    class_end_time = TimeField(verbose_name="زمان پایان دوره در روز")
    link_adr = URLField(
        verbose_name="لینک برگزاری دوره",
        default="https://nikan.iut.ac.ir/rooms/tg4-o7q-ibk-hwd/join",
    )

    def __str__(self) -> str:
        return self.name


class StudentCourse(Model):
    student = ForeignKey(verbose_name="فراگیر", to=Student, on_delete=CASCADE)
    course = ForeignKey(verbose_name="دوره", to=Course, on_delete=Course)

    def __str__(self) -> str:
        return f"{self.course} - {self.student}"
