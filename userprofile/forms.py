from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserSignupForm(UserCreationForm):
	email = forms.CharField()
	class Meta:
		model = User
		fields = ('username','email','password1','password2')