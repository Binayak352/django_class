from django.urls import path
from userprofile.views import UserLoginView, user_logout, SignupView

app_name="user"

urlpatterns = [
	path("login/", UserLoginView.as_view(), name="login"),
	path("logout/", user_logout, name="logout"),
	path("signup/",SignupView.as_view(), name = "signup"),
]