from django.shortcuts import render, redirect
from accounts.models import User
from core.forms import ProfileEditForm
from files.models import Paddock, File, Tag
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
@login_required(login_url='accounts/login')
def index(request):
    paddocks = Paddock.objects.all()
    tags = Tag.objects.all()
    files = File.objects.all().filter(deleted=0)[0:5]
    uploads = File.objects.filter(uploader=request.user, deleted=0)
    context = {'paddocks': paddocks, 'tags': tags, 'files': files, 'uploads': uploads}
    return render(request, 'core/index.html', context)

@login_required(login_url='accounts/login')
def viewProfile(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'core/profile.html', context)

@login_required(login_url='accounts/login')
def viewProfile(request,pk):
    user = User.objects.get(id=pk)
    return render(request, 'core/profile.html', {'user': user})

@login_required(login_url='accounts/login')
def editProfile(request, pk):
    user = User.objects.get(id=pk)
    if request.user.id == user or request.user.is_staff:
        if request.method == 'POST':
            form = ProfileEditForm(request.POST)
            if form.is_valid():
                user.bio = form.data['bio']
                user.save()
                return redirect('profile', pk)
        else:
            form = ProfileEditForm(initial = {
                'bio': user.bio, 
            })
        context = {'form': form}
        return render(request, 'core/edit_profile.html', context)
    else:
        return redirect('profile', request.user.id)

@login_required(login_url='accounts/login')
def search(request):
    q = request.GET.get('q')
    files = File.objects.all().filter(deleted=0)
    heading = "Results for: "
    context = {'files': files, 'heading': heading, 'heading_param': q, 'query': q}
    return render(request, 'core/browse.html', context)

@login_required(login_url='accounts/login')
def browse(request):
    files = File.objects.all().filter(deleted=0)
    heading = "All Files"
    context = {'files': files, 'heading': heading}
    return render(request, 'core/browse.html', context)

@login_required(login_url='accounts/login')
def byPaddock(request, pk):
    paddock = Paddock.objects.get(id=pk)
    files = File.objects.filter(paddocks=pk, deleted=0)
    heading = "Paddock: "
    context = {'files': files, 'heading': heading, 'heading_param': paddock}
    return render(request, 'core/browse.html', context)

@login_required(login_url='accounts/login')
def byTag(request, pk):
    tag = Tag.objects.get(id=pk)
    files = File.objects.filter(tags=pk, deleted=0)
    heading = "Tag: "
    context = {'files': files, 'heading': heading, 'heading_param': tag}
    return render(request, 'core/browse.html', context)

@login_required(login_url='accounts/login')
def byYear(request, pk):
    files = File.objects.filter(year=pk, deleted=0)
    heading = "Year: "
    context = {'files': files, 'heading': heading, 'heading_param': pk}
    return render(request, 'core/browse.html', context)


@login_required(login_url='accounts/login')
def viewRecentlyDeleted(request):
    files = File.objects.all().filter(deleted=1)
    context = {'files': files}
    return render(request, 'core/recently_deleted.html', context)

def errorPage(request):
    context = {}
    return render(request, 'core/error.html', context)


