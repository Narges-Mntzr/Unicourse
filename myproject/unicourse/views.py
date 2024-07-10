# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import (
    UserRegisterForm,
    TeacherRegisterForm,
    InstituteRegisterForm,
    StudentRegisterForm,
    LoginForm,
)
from .models import CustomUser, CustomUserType, Teacher, Institute
from django.http import JsonResponse, request


########### index#######################################
def index(request):
    return render(request, "user/index.html", {"title": "index"})


########### register#####################################


def register(request):
    user = request.POST.get("user") if request.method == "POST" else "new_user"
    print(user)
    if user != "new_user":
        user = CustomUser.objects.get(username=user)

    if request.method == "POST" and user == "new_user":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            user_type = form.cleaned_data.get("user_type")
            if user_type == CustomUserType.INSTITUTE:
                form = InstituteRegisterForm()
            elif user_type == CustomUserType.TEACHER:
                form = TeacherRegisterForm()
            else:
                form = StudentRegisterForm()
    elif request.method == "POST" and user.user_type == CustomUserType.INSTITUTE:
        form = InstituteRegisterForm(request.POST)
        if form.is_valid():
            institute = form.save(commit=False)
            institute.user = user
            institute.save()
            messages.success(
                request, f"Congratulations, your account has been successfully created."
            )
            return redirect("login")
    elif request.method == "POST" and user.user_type == CustomUserType.TEACHER:
        form = TeacherRegisterForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.user = user
            teacher.save()
            messages.success(
                request, f"Congratulations, your account has been successfully created."
            )
            return redirect("login")
    elif request.method == "POST":
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = user
            student.save()
            messages.success(
                request, f"Congratulations, your account has been successfully created."
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
        user = "new_user"
    return render(
        request,
        "user/register.html",
        {"form": form, "title": "register here", "user": user},
    )


########### login forms####################################
def loginPage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f" welcome {username} !!")
            return redirect("index")
        else:
            messages.info(request, "account done not exit plz sign in")
    form = LoginForm()
    return render(request, "user/login.html", {"form": form, "title": "log in"})


########### APIs ####################################
def getAllTeachers(request):
    teachers = list(
        Teacher.objects.values(
            "user__first_name",
            "user__email",
            "user__phone_number",
            "license",
            "national_code",
        )
    )
    return JsonResponse(teachers, safe=False)


def getAllInstitutes(request):
    institutes = list(
        Institute.objects.values(
            "user__first_name",
            "user__email",
            "user__phone_number",
            "license",
            "address",
        )
    )
    return JsonResponse(institutes, safe=False)
