from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login

def homepage(request):
    # 处理首页的请求
    return render(request, 'parcTest/homepage.html')

def listingspage(request):
    # Your view logic here
     return render(request, 'parcTest/listingspage.html')

def signuppage(request):
    # 处理注册页面的请求
    # 在这里可以添加用户注册逻辑
    if request.method == 'POST':
        # 处理用户提交的注册表单
        # 在这里可以将用户信息保存到数据库
        return HttpResponse("Registration successful")  # 重定向或显示成功消息

    return render(request, 'parcTest/signuppage.html')

def loginpage(request):
    # 处理登录页面的请求
    # 在这里可以添加用户登录逻辑
    if request.method == 'POST':
        # 处理用户提交的登录表单
        # 在这里可以验证用户信息
        return HttpResponse("Login successful")  # 重定向或显示成功消息

    return render(request, 'parcTest/loginpage.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 自动登录用户
            return redirect('homepage')  # 注册后重定向到首页或其他页面
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
