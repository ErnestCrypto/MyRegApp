# Creating a Model form
from django import forms
from django.forms import ModelForm
from .models import User
from django import forms


class UserForm(ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username', 'email_address', 'telephone',
            'password1', 'password2',
        ]
