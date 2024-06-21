from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("register/learner", views.registerLearner, name="register"),
    path("register/teacher", views.registerTeacher, name="register"),
    path("register/institute", views.registerInstitute, name="register"),
]
