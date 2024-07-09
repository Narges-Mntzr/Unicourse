from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Teacher, Institute, Student, CustomUserType, SchoolTypeChoices

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label=False, widget=forms.TextInput(attrs={"placeholder": "Username*"})
    )
    email = forms.EmailField(
        label=False, widget=forms.EmailInput(attrs={"placeholder": "Email*"})
    )
    phone_number = forms.CharField(
        label=False,
        max_length=11,
        widget=forms.TextInput(attrs={"placeholder": "Phone Number*"}),
    )
    password1 = forms.CharField(
        label=False, widget=forms.PasswordInput(attrs={"placeholder": "Password*"})
    )
    password2 = forms.CharField(
        label=False,
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password*"}),
    )
    first_name = forms.CharField(
        label=False,
        max_length=20,
        widget=forms.TextInput(attrs={"placeholder": "Name*"}),
    )
    user_type = forms.ChoiceField(
        label=False,
        choices=CustomUserType.choices,
        widget=forms.Select(attrs={"placeholder": "Role*"}),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "phone_number",
            "password1",
            "password2",
            "first_name",
            "user_type",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style = "background-color: #BDBDBD;color: black; height:50px; border-radius: 10px; margin:20px;"
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update(
                {"class": "form-control custom-placeholder", "style": style}
            )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError({"password2": "Passwords do not match"})

        return cleaned_data


class TeacherRegisterForm(forms.ModelForm):
    national_code = forms.CharField(
        label=False,
        max_length=15,
        widget=forms.TextInput(attrs={"placeholder": "National Code*"}),
    )
    license = forms.CharField(
        label=False,
        max_length=30,
        widget=forms.TextInput(attrs={"placeholder": "License Code*"}),
    )

    class Meta:
        model = Teacher
        fields = ["national_code", "license"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style = "background-color: #BDBDBD;color: black; height:50px; border-radius: 10px; margin:20px;"
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update(
                {"class": "form-control custom-placeholder", "style": style}
            )


class InstituteRegisterForm(forms.ModelForm):
    address = forms.CharField(
        label=False,
        max_length=200,
        widget=forms.TextInput(attrs={"placeholder": "Address*"}),
    )
    license = forms.CharField(
        label=False,
        max_length=30,
        widget=forms.TextInput(attrs={"placeholder": "License Code*"}),
    )

    class Meta:
        model = Institute
        fields = ["license", "address"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style = "background-color: #BDBDBD;color: black; height:50px; border-radius: 10px; margin:20px;"
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update(
                {"class": "form-control custom-placeholder", "style": style}
            )


class StudentRegisterForm(forms.ModelForm):
    birthday = forms.DateField(
        label=False, widget=forms.TextInput(attrs={"placeholder": "Birthday*"})
    )
    school = forms.CharField(
        label=False,
        max_length=30,
        widget=forms.TextInput(attrs={"placeholder": "School Name*"}),
    )
    type_of_school = forms.ChoiceField(
        label=False,
        choices=SchoolTypeChoices.choices,
        widget=forms.Select(attrs={"placeholder": "School Type*"}),
    )

    class Meta:
        model = Student
        fields = ["birthday", "school", "type_of_school"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style = "background-color: #BDBDBD;color: black; height:50px; border-radius: 10px; margin:20px;"
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update(
                {"class": "form-control custom-placeholder", "style": style}
            )


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"placeholder": "Username*"})
        self.fields["password"].widget.attrs.update({"placeholder": "Password*"})

        style = "background-color: #BDBDBD;color: black; height:50px; border-radius: 10px; margin:20px; width: 40%;"
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update(
                {"class": "form-control custom-placeholder", "style": style}
            )
            self.fields[field_name].label = False
