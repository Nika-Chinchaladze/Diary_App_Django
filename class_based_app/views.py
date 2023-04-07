from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.views.generic.edit import CreateView

from .models import Diary
from .forms import LoginForm, RegistrationForm
# Create your views here.


class LoginView(View):
    form_class = LoginForm
    initial = {"key": "value"}
    template_name = "diary_app/login.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {
            "form": form
        })
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                return HttpResponseRedirect(reverse("login"))


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, "diary_app/logout.html")


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = "diary_app/register.html"
    form_class = RegistrationForm
    success_message = "Congratulations, your profile has been created successfully!"
    success_url = reverse_lazy("login")


def home_view(request):
    return render(request, "diary_app/home.html")