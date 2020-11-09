from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import  CreateView
from userprofile.forms import UserSignupForm


# def login_view(request):
#     form = AuthenticationForm(request.POST or None)
#     if request.POST:
#         user = authenticate(username = request.POST['username'], password = request.POST['password'])
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse("app:home"))
#     return render(request, "login.html", {"form": form})

class UserLoginView(LoginView):
	login_url = "user:login"
	template_name = "login.html"
	authentication_form = AuthenticationForm
	redirect_authenticated_user = True

	def get_success_url(self):
		return reverse("app:home")

class SignupView(CreateView):
	model = User
	template_name = "signup.html"
	form_class = UserSignupForm

	def form_valid(self, form):
		super().form_valid(form)
		user = authenticate(username=form.cleaned_data.get("username"), password = form.cleaned_data.get("password1"))
		login(self.request, user)
		return redirect(reverse("app:home"))

	def get_success_url(self):
		return reverse("user:login")

def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse("user:login"))
