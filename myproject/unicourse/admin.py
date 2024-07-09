from django.contrib import admin
from .models import CustomUser, Teacher, Institute, Student


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "user_type")


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "national_code", "license")


@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display = ("user", "license", "address")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
