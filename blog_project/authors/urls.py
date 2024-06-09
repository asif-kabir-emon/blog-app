from django.urls import path
from .views import user_registration, user_login, user_logout, profile, change_password
from django.contrib.auth.views import LogoutView
from .views import UserLoginView, UserLogoutView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register/", user_registration, name="register"),
    # path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("login/", UserLoginView.as_view(), name="login"),
    # path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
    path("profile/change_password/", change_password, name="change_password"),
]