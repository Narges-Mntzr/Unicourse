from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm
from .models import Teacher

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	phone_number = forms.CharField(max_length = 11)
	first_name = forms.CharField(max_length = 20)
	last_name = forms.CharField(max_length = 20)
	class Meta:
		model = User
		fields = ['username', 'email', 'phone_number', 'password1', 'password2', 'first_name', 'last_name']

class TeacherRegisterForm(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = ['user', 'national_code', 'license']