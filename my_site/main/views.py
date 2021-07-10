from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import NewUserForm


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            return redirect("main:home")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    form = NewUserForm()
    return render(request, 'main/register.html', {'form': form})


def detail1(request):
    return render(request, 'main/detail1.html')


def detail2(request):
    return render(request, 'main/detail2.html')


def detail3(request):
    return render(request, 'main/detail3.html')


def detail4(request):
    return render(request, 'main/detail4.html')


def detail5(request):
    return render(request, 'main/detail5.html')


def detail6(request):
    return render(request, 'main/detail6.html')
