from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateView, ProfileView, UserLoginView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("profile/", login_required(ProfileView.as_view()), name="profile"),
    # path("reset_password/", reset_password, name="reset_password"),
    # path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
]
