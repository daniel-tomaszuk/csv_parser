from django import forms
from django.core.validators import *
from django.core.exceptions import *
from .models import *

class Login(forms.Form):
    login = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)

