from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, ProfileForm, UserLoginForm
from users.models import User
import secrets


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")


class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
