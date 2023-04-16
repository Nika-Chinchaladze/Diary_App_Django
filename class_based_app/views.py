from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
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


class HomeView(View):
    def get(self, request):
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


class AddNoteView(FormView):
    template_name = "diary_app/new.html"
    form_class = DiaryModelForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.save()
        return super(AddNoteView, self).form_valid(form)


class AddImageView(FormView):
    template_name = "diary_app/user_image.html"
    form_class = ImageModelForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.save()
        return super(AddImageView, self).form_valid(form)


class AddBackgroundView(FormView):
    template_name = "diary_app/background_image.html"
    form_class = BackgroundModelForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.save()
        return super(AddBackgroundView, self).form_valid(form)


class NoteDetailView(DetailView):
    model = Diary
    template_name = "diary_app/detail.html"
    context_object_name = "note"


class NoteListView(ListView):
    model = Diary
    template_name = "diary_app/all.html"
    context_object_name = "notes"

    def get_queryset(self):
        result = super(NoteListView, self).get_queryset()
        current_user = self.request.user
        result = Diary.objects.filter(user=current_user).all().order_by("-date_time")
        return result


class NoteUpdateView(UpdateView):
    model = Diary
    fields = ["title", "image_url", "content"]
    template_name = "diary_app/update.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        return super(NoteUpdateView, self).form_valid(form)


class NoteDeleteView(DeleteView):
    model = Diary
    template_name = "diary_app/diary_confirm_delete.html"
    context_object_name = "note"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        return super(NoteDeleteView, self).form_valid(form)
