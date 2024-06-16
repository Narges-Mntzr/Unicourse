from django.contrib import admin
from .models import CustomUser, Teacher


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "user_type")


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "national_code", "license")
    search_fields = ["user"]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Teacher, TeacherAdmin)
