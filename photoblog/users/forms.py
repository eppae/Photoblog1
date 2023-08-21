from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username= forms.CharField(max_length=40)
    password = forms.CharField(max_length=40,widget=forms.PasswordInput)



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password','email']