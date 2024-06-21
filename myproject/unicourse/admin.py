from django.contrib import admin
from .models import CustomUser, Teacher, Institute


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "user_type")


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "national_code", "license")


class InstituteAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "license", "address")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Institute, InstituteAdmin)
