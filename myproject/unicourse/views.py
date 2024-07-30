from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import (
    UserRegisterForm,
    TeacherRegisterForm,
    InstituteRegisterForm,
    StudentRegisterForm,
    LoginForm,
    AddCourseForm,
)
from django.utils.timezone import now
from .models import (
    CustomUser,
    CustomUserType,
    Teacher,
    Institute,
    Course,
    Student,
    StudentCourse,
)
from django.http import JsonResponse


########### index#######################################
def index(request):
    if not request.user.is_authenticated:
        return render(request, "user/index.html", {"title": "index"})
    elif request.user.user_type == CustomUserType.INSTITUTE:
        institute = Institute.objects.get(user=request.user)
        courses = Course.objects.filter(institute=institute).select_related(
            "teacher", "teacher__user"
        )
        return render(
            request,
            "institute_courses.html",
            {"institute": institute, "courses": courses},
        )
    elif request.user.user_type == CustomUserType.STUDENT:
        student = Student.objects.get(user=request.user)
        student_courses = StudentCourse.objects.filter(student=student).select_related(
            "course", "course__teacher", "course__teacher__user"
        )
        return render(
            request,
            "student_courses.html",
            {"student_courses": student_courses, "now": now()},
        )


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
                request, "Congratulations, your account has been successfully created."
            )
            return redirect("index")
    elif request.method == "POST" and user.user_type == CustomUserType.TEACHER:
        form = TeacherRegisterForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.user = user
            teacher.save()
            messages.success(
                request, "Congratulations, your account has been successfully created."
            )
            return redirect("index")
    elif request.method == "POST":
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = user
            student.save()
            messages.success(
                request, "Congratulations, your account has been successfully created."
            )
            return redirect("index")
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


def addCourseInstitute(request):
    if not request.user.is_authenticated:
        messages.info(request, "You are not logged in.")
        return redirect("login")
    if request.user.user_type != CustomUserType.INSTITUTE:
        messages.info(request, "user is not institute.")
        return redirect("login")
    if request.method == "POST":
        institute = Institute.objects.get(user=request.user)
        form = AddCourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.institute = institute
            course.save()
            messages.success(
                request, "Congratulations, your course has been successfully created."
            )
            return redirect("index")
        else:
            messages.info(request, "Form is not valid.")

    form = AddCourseForm()
    return render(
        request, "create_course.html", {"form": form, "title": "add new course"}
    )


def listCourseStudent(request):
    if not request.user.is_authenticated:
        messages.info(request, "You are not logged in.")
        return redirect("login")
    student = student = Student.objects.get(user=request.user)
    courses = Course.objects.all().select_related("teacher", "teacher__user")
    enrolled_courses = StudentCourse.objects.filter(student=student).values_list(
        "course_id", flat=True
    )
    return render(
        request,
        "all_courses.html",
        {"courses": courses, "enrolled_courses": enrolled_courses},
    )


def getCourseStudent(request, course_id):
    student = student = Student.objects.get(user=request.user)
    course = get_object_or_404(Course, id=course_id)
    StudentCourse.objects.create(student=student, course=course)
    messages.success(request, f"You have successfully enrolled in {course.name}.")
    return redirect("list_course_student")
