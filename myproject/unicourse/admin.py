from django.contrib import admin
from django.core.mail import send_mail
from .models import CustomUser, Teacher, Institute, Student, Course, StudentCourse


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
                "Institute Approved",
                "Welcome to Unicourse! I'm Shirin 🌚, your personal assistant, how can I help you?",
                "from@unicourse.com",
                [email],
                fail_silently=False,
            )

        super().save_model(request, obj, form, change)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    pass
