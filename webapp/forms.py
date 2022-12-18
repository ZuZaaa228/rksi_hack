from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from .models import CustomUser


# from .models import User

class UserLoginForm(AuthenticationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': "form-styling", 'type': "text", "name": "username", "placeholder": "",
    # }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
         'class': "form-styling", 'type': "text", "name":"username", "placeholder": "",
     }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-styling", 'type': "text", "name":"username", "placeholder": "",
        "autocomplete": "current-password",
    }))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password',]

class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('FIO','password', 'email',)