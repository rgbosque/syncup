from django.contrib.auth import get_user_model, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UserLoginForm, UserCreationForm

User = get_user_model()


def user_login(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        uname_ = form.cleaned_data.get('username')
        user_obj = User.objects.get(username__iexact=uname_)
        login(request, user_obj)
        return HttpResponseRedirect('/')

    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def register(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/accounts/login')

    return render(request, 'accounts/register.html', {'form': form})
