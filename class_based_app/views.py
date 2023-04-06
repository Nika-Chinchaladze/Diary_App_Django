from django.shortcuts import render

# Create your views here.

def login_view(request):
    return render(request, "diary_app/login.html")