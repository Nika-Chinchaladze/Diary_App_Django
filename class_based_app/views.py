from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

from .models import Diary, Image, Background
from .forms import LoginForm, RegistrationForm, DiaryModelForm, ImageModelForm, BackgroundModelForm
# Create your views here.


class LoginView(View):
    form_class = LoginForm
    initial = {"key": "value"}
    template_name = "diary_app/login.html"

    def get(self, request, *args, **kwargs):
        current_user = request.user
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {
            "form": form,
            "user": current_user
        })
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("home"))
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
    current_user = request.user
    notes = Diary.objects.filter(user=current_user).all().order_by("-date_time")
    image = Image.objects.filter(user=current_user).first()
    background = Background.objects.filter(user=current_user).first()
    return render(request, "diary_app/home.html", {
        "notes": notes[:3],
        "user": current_user,
        "image": image,
        "background": background
    })


def add_note_view(request):
    current_user = request.user
    if request.method == "POST":
        form = DiaryModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
    form = DiaryModelForm()
    return render(request, "diary_app/new.html", {
        "form": form,
        "user": current_user
    })


def add_image_view(request):
    current_user = request.user
    if request.method == "POST":
        form = ImageModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
    form = ImageModelForm()
    return render(request, "diary_app/user_image.html", {
        "form": form,
        "user": current_user
    })


def add_background_view(request):
    current_user = request.user
    if request.method == "POST":
        form = BackgroundModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
    form = BackgroundModelForm()
    return render(request, "diary_app/background_image.html", {
        "form": form,
        "user": current_user
    })


def note_detail_view(request, note_id):
    current_user = request.user
    chosen_note = Diary.objects.get(id=note_id)
    return render(request, "diary_app/detail.html", {
        "note": chosen_note,
        "user": current_user
    })


def note_all_view(request):
    current_user = request.user
    notes = Diary.objects.filter(user=current_user).all()
    return render(request, "diary_app/all.html", {
        "notes": notes,
        "user": current_user
    })


def note_update_view(request, note_id):
    current_user = request.user
    chosen_note = Diary.objects.get(id=note_id)
    
    if request.method == "POST":
        form = DiaryModelForm(request.POST)
        if form.is_valid():
            chosen_note.title = form.cleaned_data["title"]
            chosen_note.image_url = form.cleaned_data["image_url"]
            chosen_note.content = form.cleaned_data["content"]
            chosen_note.save()
            return HttpResponseRedirect(reverse("home"))

    initial_data = {
        "title": chosen_note.title,
        "image_url": chosen_note.image_url,
        "content": chosen_note.content,
        "user": chosen_note.user
    }
    form = DiaryModelForm(initial=initial_data)
    return render(request, "diary_app/update.html", {
        "note": chosen_note,
        "user": current_user,
        "form": form
    })


def note_delete_view(request, note_id):
    chosen_note = Diary.objects.get(id=note_id)
    chosen_note.delete()
    return HttpResponseRedirect(reverse("home"))
