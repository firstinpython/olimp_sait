from django.urls import path
from .views import registration, authtorization,profile

app_name = "users"

urlpatterns = [
    path("auth/",authtorization, name="auth"),
    path("login/",registration, name = "login"),
    path("profile",profile, name="profile")
]