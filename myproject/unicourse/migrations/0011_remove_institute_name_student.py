# Generated by Django 5.0.6 on 2024-07-09 16:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("unicourse", "0010_institute_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="institute",
            name="name",
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("birthday", models.DateField(verbose_name="تاریخ تولد")),
                ("school", models.TextField(max_length=30, verbose_name="اسم مدرسه")),
                (
                    "type_of_school",
                    models.TextField(
                        choices=[
                            ("high", "دبیرستان"),
                            ("middle", "راهنمایی"),
                            ("elementary", "دبستان"),
                        ],
                        default="elementary",
                        max_length=20,
                        verbose_name="مقطع تحصیلی",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Student",
                "verbose_name_plural": "Students",
            },
        ),
    ]
