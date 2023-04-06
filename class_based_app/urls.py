from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("logout", views.LogoutView.as_view(), name="logout")
]
