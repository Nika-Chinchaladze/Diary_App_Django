from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.LoginView.as_view(), name="login"),
    path("logout", login_required(views.LogoutView.as_view()), name="logout"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("home", views.home_view, name="home"),
    path("new", views.add_note_view, name="new"),
    path("user-image", views.add_image_view, name="user-image"),
    path("background-image", views.add_background_view, name="background-image")
]
