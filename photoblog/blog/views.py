from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages  #진행상태를 메시지로 폼에서 출력하고 싶을 때 사용
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    render(request,'account/auth-login-basic.html')