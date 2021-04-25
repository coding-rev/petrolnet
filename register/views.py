from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from .forms import RegisterForm

from django.contrib import messages

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegisterForm()

    return render(response, "register.html", {"form":form})
