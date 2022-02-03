# Creating our views
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .form import UserForm
from django.contrib import messages


def homePage(request):

    return render(request, 'app/home.html', )


def registerPage(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(
                    request, f'Hi {username} your account was created successfully.')
            else:
                form = UserForm()
                messages.error(
                    request, 'Failed to create account. Please check your details')
        else:
            messages.error(
                request, 'Please make sure the passwords are the same in both fields')
    else:
        form = UserForm()
        messages.error(request, 'Failed to add user')
    context = {'form': form}
    return render(request, 'app/register.html', context)


def loginPage(request):
    form = UserForm()

    context = {'form': form}
    return render(request, 'app/login.html', context)
