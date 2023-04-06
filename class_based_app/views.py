from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View

from .models import Diary
from .forms import LoginForm
# Create your views here.


def login_view(request):
    form = LoginForm()
    return render(request, "diary_app/login.html", {
        "form": form
    })


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, "diary_app/logout.html")

