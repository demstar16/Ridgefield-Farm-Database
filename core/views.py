from django.shortcuts import render, redirect
from accounts.models import User
from files.models import Paddock, File
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='accounts/login')
def index(request):
    paddocks = Paddock.objects.all()
    files = File.objects.all()[0:5]
    context = {'paddocks': paddocks, 'files': files}
    return render(request, 'core/index.html', context)

@login_required(login_url='accounts/login')
def viewProfile(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'core/profile.html', context)

@login_required(login_url='accounts/login')
def search(request):
    q = request.GET.get('q')
    files = File.objects.all().filter(deleted=0)
    heading = "Results for: "
    showpaddock = True
    context = {'files': files, 'showpaddock': showpaddock,
        'heading': heading, 'heading_param': q, 'query': q}
    return render(request, 'core/browse.html', context)

@login_required(login_url='accounts/login')
def browse(request):
    files = File.objects.all().filter(deleted=0)
    heading = "All Files"
    showpaddock = True
    context = {'files': files, 'showpaddock': showpaddock, 'heading': heading}
    return render(request, 'core/browse.html', context)

@login_required(login_url='accounts/login')
def byPaddock(request, pk):
    paddock = Paddock.objects.get(id=pk)
    files = File.objects.filter(paddocks=pk)
    heading = "Paddock: "
    showpaddock = False
    context = {'files': files, 'showpaddock': showpaddock,
        'heading': heading, 'heading_param': paddock}
    return render(request, 'core/browse.html', context)


@login_required(login_url='accounts/login')
def viewRecentlyDeleted(request):
    files = File.objects.all().filter(deleted=1)
    context = {'files': files}
    return render(request, 'core/recently_deleted.html', context)
