from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.LoginView.as_view(), name="login"),
    path("logout", login_required(views.LogoutView.as_view()), name="logout"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("home", views.HomeView.as_view(), name="home"),
    path("new", views.AddNoteView.as_view(), name="new"),
    path("user-image", views.AddImageView.as_view(), name="user-image"),
    path("back-image", views.AddBackgroundView.as_view(), name="back-image"),
    path("detail/<int:pk>", views.NoteDetailView.as_view(), name="detail"),
    path("update/<int:pk>", views.NoteUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", views.NoteDeleteView.as_view(), name="delete"),
    path("all", views.NoteListView.as_view(), name="all")
]
