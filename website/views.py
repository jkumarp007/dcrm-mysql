from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SingUpForm

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
        else:
            messages.warning(request, 'Invalid username or password')
        return redirect('/login')
    else:
        return render(request, 'login.html')


def logout_user(request):
    print('logout')
    try:
        logout(request)
        messages.success(request, 'You have been logged out')
    except Exception as e:
        print(e)
    return redirect('/')


def register_user(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)

        if form.is_valid():
            form.save()

            # authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            """ 
            username = request.POST.get('username')
            password = request.POST.get('password')
            """
            # authenticate
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered. Welcome!')
            return redirect('/')
    else:
        form = SingUpForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})
