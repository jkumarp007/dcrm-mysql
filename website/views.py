from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SingUpForm, AddRecordForm
from .models import Record

# Create your views here.


def home(request):
    records = Record.objects.all()
    return render(request, 'home.html', {'records': records})


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
            # authenticate
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(
                request, 'You have successfully registered. Welcome!')
            return redirect('/')
    else:
        form = SingUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def record_view(request, record_id):
    record = None
    try:
        record = Record.objects.get(id=record_id)
    except Exception as e:
        print(e)
    return render(request, 'record.html', {'record': record})


def record_delete(request, record_id):
    try:
        Record.objects.get(id=record_id).delete()
        messages.success(
            request, 'Record deleted successfully')
    except Exception as e:
        print(e)
    return redirect('/')


def record_add(request):
    form = AddRecordForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            add_record = form.save()
            messages.success(request, 'Record added successfully')
            return redirect('/')
        
    return render(request, 'record_add.html', {'form': form })

def record_edit(request, record_id):
    current_record = Record.objects.get(id=record_id)
    form = AddRecordForm(request.POST or None, instance=current_record)
    if request.method == 'POST':
        if form.is_valid():
            add_record = form.save()
            messages.success(request, 'Record updated successfully')
            return redirect('/')
        
    return render(request, 'record_edit.html', {'form': form, 'record':current_record })
