from django.contrib import admin
from django.core.mail import send_mail
from .models import CustomUser, Teacher, Institute, Student


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "user_type")


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "national_code", "license")


@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display = ("user", "license", "address", "is_approved")

    def save_model(self, request, obj, form, change):
        if change and obj.is_approved:
            email = obj.user.email
            
            send_mail(
                'Institute Approved',
                'Your institute has been approved. Welcome to Unicourse!',
                'from@unicourse.com',
                [email],
                fail_silently=False,
            )

        super().save_model(request, obj, form, change)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
