from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.LoginView.as_view(), name="login"),
    path("logout", login_required(views.LogoutView.as_view()), name="logout"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("home", views.home_view, name="home")
]
