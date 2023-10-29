from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate, login

def homepage(request):
    return render(request, 'parcTest/homepage.html')

def listingspage(request):
     return render(request, 'parcTest/listingspage.html')

def signuppage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('homepage')  
    else:
        form = UserCreationForm()
    return render(request, 'parcTest/signuppage.html', {'form': form})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('parcTest:userpage')
        else:
            return render(request, 'parcTest/loginpage.html', {'error_message': 'Invalid username or password'})
    
    return render(request, 'parcTest/loginpage.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('homepage')  
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def userpage(request):
    return render(request, 'parcTest/userpage.html')
