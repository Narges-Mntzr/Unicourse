from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("api/teachers/", views.getAllTeachers, name="get_all_teachers"),
]
