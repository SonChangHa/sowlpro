from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms


class SigninForm(ModelForm):  # 로그인을 제공하는 class.

    class Meta:
        model = User
        widgets = {'password': forms.PasswordInput}
        fields = ['username', 'password']
