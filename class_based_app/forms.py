from django import forms


class LoginForm(forms.Form):
    user_email = forms.EmailField(max_length=200)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput())