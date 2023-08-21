from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'accounts/auth-login-basic',{'form':form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username,password=password)
            if user:
                login(request,user)
                messages.success(
                    request,f'{username.title()}님 로그인을 환영합니다!')
                return redirect('main')
        messages.error(request,f'유효하지 않은 id나 password입니다')
        return render(request, 'users/auth-login-basic.html',{'form':form})

def sign_out(request):
    logout(request)
    messages.success(request,f'로그아웃에 성공하였습니다')
def sign_up(request):
    if request.method =='GET':
        form = RegisterForm()
        return render(request,'users/auth-register-basic.html',{'form':form})
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,"회원가입 성공")
            login(request,user)
            return redirect('main')
        else:
            return render(request,'users/auth-register-basic.html',{'form':form})
