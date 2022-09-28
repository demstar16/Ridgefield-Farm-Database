from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from accounts.forms import AccessRequestForm
from django.http.response import HttpResponseRedirect
from django.views.generic.base import View
# Create your views here.
from accounts.models import User
from django.urls import reverse


def register(request):
    if request.method == 'POST':
        form = AccessRequestForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('submitted')
    else:
        form = AccessRequestForm()
    return render(request, 'registration/register.html', {'form': form})


def submitted(request):
    return render(request, 'registration/request_sent.html')


# user list
def audit_list(request):
    users = User.objects.all()
    user_list = []
    for user in users:
        user_list.append(user.to_dict())
    return render(request, 'registration/audit_account.html', {'users': users})


# Aduit passed
def audit_activate(request, pk):
    user = User.objects.get(id=int(pk))
    user.is_active = 1
    user.save()
    users = User.objects.all()
    user_list = []
    for user in users:
        user_list.append(user.to_dict())
    return render(request, 'registration/audit_account.html', {'users': users})


# Audit not passed
def audit_freeze(request, pk):
    user = User.objects.get(id=int(pk))
    user.is_active = 0
    user.save()
    users = User.objects.all()
    user_list = []
    for user in users:
        user_list.append(user.to_dict())
    return render(request, 'registration/audit_account.html', {'users': users})


