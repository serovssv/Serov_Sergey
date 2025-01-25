from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about-us-1.html')


def blog(request):
    return render(request, 'main/blog.html')


def nocr1(request):
    return render(request, 'main/nocr-1.html')


def nocr2(request):
    return render(request, 'main/nocr-2.html')


def nocr3(request):
    return render(request, 'main/nocr-3.html')


def nocr4(request):
    return render(request, 'main/nocr-4.html')


def nocr5(request):
    return render(request, 'main/nocr-5.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def profile_view(request):
    return render(request, 'main/profile.html')
