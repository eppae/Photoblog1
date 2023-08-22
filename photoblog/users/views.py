from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse
# Create your views here.
def sign_in(request):
    if request.method == 'GET':
        remembered_username = request.session.get('remembered_username', '')
        #form = LoginForm()
        return render(request,'account/auth-login-basic.html',{'rememebered_username':remembered_username})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            print(form.errors)
        elif form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_id = request.POST.get('remember-id')
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request,user)
                response = redirect('main')
                if remember_id:
                    response.set_cookie('remembered_username',username,max_age=(3600*24*1))
                else:
                    response.delete_cookie('remembered_username')
                messages.success(request,f'{username.title()}님 로그인을 환영합니다!')
                return response
        else:
            messages.error(request,f'유효하지 않은 id나 password 입니다')
            return render(request, 'account/auth-login-basic.html')#,{'form':form})
def edit_profile(request):
    if request.user.is_authenticated:
        return render(request,'account/pages-account-settings-account.html')
    else:
        messages.success(
            request, f'정보 수정을 하려면 로그인을 하셔야 합니다')
        return render(request,'account/auth-login-basic.html')

def sign_out(request):
    logout(request)
    messages.success(request,f'로그아웃 성공')
    return redirect(reverse('main'))
def sign_up(request):
    if request.method =='GET':
        #form = RegisterForm()
        return render(request,'account/auth-register-basic.html')#,{'form':form})
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,"회원가입 성공")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request,user)
                return redirect('main')
        else:
            return render(request,'account/auth-register-basic.html')#{'form':form})

def forgot(request):
    if request.method =='GET':
        return render(request,'account/auth-forgot-password-basic.html')
    if request.method =='POST':
        form = PasswordResetForm(request.POST)
        if not form.is_valid():
            print(form.errors)
        elif form.is_valid():
            form.save(
                request=request,
                from_email='cinester@naver.com',
                email_template_name='account/auth-password-reset.html'
            )
        else:
            form = PasswordResetForm()
        return render(request,'account/auth-forgot-password-basic.html')
def password_reset(request):
    pass