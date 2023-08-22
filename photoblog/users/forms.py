from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=40)
    password = forms.CharField(label='Password',max_length=40,widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email address', max_length=254, required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class PasswordReset(PasswordResetForm):
    class Meta:
        model = User
        fields = ['email']