from django.contrib import admin
from .models import CustomUser, Teacher


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "user_type")


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "national_code", "license")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Teacher, TeacherAdmin)
