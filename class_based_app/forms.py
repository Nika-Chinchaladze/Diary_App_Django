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

        self.fields["first_name"].max_length = 150
        self.fields["last_name"].max_length = 150
        self.fields["username"].max_length = 150
        self.fields["email"].max_length = 150
        self.fields["password1"].max_length = 150
        self.fields["password2"].max_length = 150
    
    def password_similarity(self):
        password_1 = self.cleaned_data["password1"]
        password_2 = self.cleaned_data["password2"]

        if password_1 != password_2:
            raise forms.ValidationError("Invalid Data")

        return True



class DiaryModelForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ("title", "image_url", "content", "user",)
    
    def __init__(self, *args, **kwargs):
        super(DiaryModelForm, self).__init__(*args, **kwargs)

        self.fields["title"].label = ""
        self.fields["content"].label = ""
        self.fields["image_url"].label = ""
        self.fields["user"].label = "Author"

        self.fields["title"].widget.attrs["placeholder"] = "Title"
        self.fields["content"].widget.attrs["placeholder"] = "Diary Content"
        self.fields["image_url"].widget.attrs["placeholder"] = "Image Link"


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
        