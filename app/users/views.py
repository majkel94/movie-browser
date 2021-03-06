from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.forms import SignUpForm


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if not form.is_valid():
            messages.error(request, form.errors)
        else:
            form.save()
            messages.success(request, "An account has been created!")
            return redirect("login")

    context = {"form": SignUpForm()}
    return render(request, "register_page.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            to = request.POST.get('next', 'home')
            return redirect(to)
        else:
            messages.error(request, "Invalid credentials!")

    context = {}
    return render(request, "login_page.html", context)


@login_required(login_url="login")
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect("login")


@login_required(login_url="login")
def home(request):
    return redirect('search')
