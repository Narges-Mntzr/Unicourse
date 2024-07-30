from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("api/teachers/", views.getAllTeachers, name="get_all_teachers"),
    path("api/institutes/", views.getAllInstitutes, name="get_all_institutes"),
    path("course/add", views.addCourseInstitute, name="add_course"),
    path("course/get", views.listCourseStudent, name="list_course_student"),
    path("course/get/<int:course_id>/", views.getCourseStudent, name="get_course"),
]
