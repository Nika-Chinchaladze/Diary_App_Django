from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Diary, Image, Background


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150, required=True, 
        label="", 
        widget=forms.TextInput(attrs={"placeholder": "username"})
        )
    password = forms.CharField(
        max_length=150, required=True, 
        label="", 
        widget=forms.PasswordInput(attrs={"placeholder": "password"})
        )


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=1000, required=False)
    last_name = forms.CharField(max_length=1000, required=False)
    email = forms.EmailField(max_length=1000, required=False)
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2",)
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields["first_name"].label = ""
        self.fields["last_name"].label = ""
        self.fields["username"].label = ""
        self.fields["email"].label = ""
        self.fields["password1"].label = ""
        self.fields["password2"].label = ""

        self.fields["first_name"].widget.attrs["placeholder"] = "first name"
        self.fields["last_name"].widget.attrs["placeholder"] = "last name"
        self.fields["username"].widget.attrs["placeholder"] = "username"
        self.fields["email"].widget.attrs["placeholder"] = "email"
        self.fields["password1"].widget.attrs["placeholder"] = "password 1"
        self.fields["password2"].widget.attrs["placeholder"] = "password 2"


class DiaryModelForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ("title", "content", "user",)
    
    def __init__(self, *args, **kwargs):
        super(DiaryModelForm, self).__init__(*args, **kwargs)

        self.fields["title"].label = ""
        self.fields["content"].label = ""
        self.fields["user"].label = "Author"

        self.fields["title"].widget.attrs["placeholder"] = "title"
        self.fields["content"].widget.attrs["placeholder"] = "Diary Content"


class ImageModelForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("image", "user",)
    
    def __init__(self, *args, **kwargs):
        super(ImageModelForm, self).__init__(*args, **kwargs)

        self.fields["image"].label = ""
        self.fields["user"].label = ""



class BackgroundModelForm(forms.ModelForm):
    class Meta:
        model = Background
        fields = ("image", "user",)
    
    def __init__(self, *args, **kwargs):
        super(BackgroundModelForm, self).__init__(*args, **kwargs)

        self.fields["image"].label = ""
        self.fields["user"].label = ""
        