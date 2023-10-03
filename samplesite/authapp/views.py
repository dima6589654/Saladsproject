from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods

from authapp.forms import UserLoginForm, RegisterUserForm


@require_http_methods(["POST"])
def login(request):
    title = "Вход"
    form = UserLoginForm(data=request.POST)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = auth.authenticate(username=username, password=password)

        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse_lazy('index'))

    context = {
        'title': title,
        'form': form,
    }

    return render(request, 'authapp/login.html', context)


@require_http_methods(["POST"])
def register(request):
    title = "Регистрация"

    if request.method == 'POST':
        form = RegisterUserForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('authapp:login'))
    else:
        form = RegisterUserForm()

    context = {
        'title': title,
        'form': form,
    }

    return render(request, 'authapp/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse_lazy('index'))
