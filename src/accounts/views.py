from django.contrib.auth import get_user_model, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UserLoginForm

User = get_user_model()


def user_login(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        uname_ = form.cleaned_data.get('username')
        user_obj = User.objects.get(username__iexact=uname_)
        login(request, user_obj)
        return HttpResponseRedirect('/dashboard')

    context = {"form": form}
    return render(request, 'accounts/login.html', context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')
