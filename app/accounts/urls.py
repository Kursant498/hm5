from django.urls import path

from app.accounts.views import RegisterView, LoginView, LogoutView, Profile

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", Profile.as_view(), name="profile")
]
