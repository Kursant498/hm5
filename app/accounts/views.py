from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from .forms import RegisterForm

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")

class LoginView(LoginView):
    template_name = "accounts/login.html"

class LogoutView(LogoutView):
    next_page = reverse_lazy("login")

class Profile(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/profile.html"
    context_object_name = "user_profile"

    def get_object(self, queryset=None):
        return self.request.user