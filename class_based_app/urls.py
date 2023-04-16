from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.LoginView.as_view(), name="login"),
    path("logout", login_required(views.LogoutView.as_view(), login_url="/"), name="logout"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("home", login_required(views.HomeView.as_view(), login_url="/"), name="home"),
    path("new", login_required(views.AddNoteView.as_view(), login_url="/"), name="new"),
    path("user-image", login_required(views.AddImageView.as_view(), login_url="/"), name="user-image"),
    path("back-image", login_required(views.AddBackgroundView.as_view(), login_url="/"), name="back-image"),
    path("detail/<int:pk>", login_required(views.NoteDetailView.as_view(), login_url="/"), name="detail"),
    path("update/<int:pk>", login_required(views.NoteUpdateView.as_view(), login_url="/"), name="update"),
    path("delete/<int:pk>", login_required(views.NoteDeleteView.as_view(), login_url="/"), name="delete"),
    path("all", login_required(views.NoteListView.as_view(), login_url="/"), name="all")
]
