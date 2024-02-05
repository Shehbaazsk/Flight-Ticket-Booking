from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email","password1","password1")


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
