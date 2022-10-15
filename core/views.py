from django.shortcuts import render, redirect
from accounts.models import User
from core.forms import BioForm
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

# @login_required(login_url='accounts/login')
# def editProfile(request):
#     if request.method == "POST":
#         form = BioForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = BioForm(instance=request.user)
#         args = {'form':form} 
#         return render(request, 'core/profile.html', args)

@login_required(login_url='accounts/login')
def viewProfile(request,pk):
    user = User.objects.get(id=pk)
    form = BioForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user.bio = request.POST['bio']
            user.save()
            return redirect('profile', pk=pk)
    return render(request, 'core/profile.html', {'user': user, "form": form})

# @login_required(login_url='accounts/login')
# def editProfile(request):
#     if request.method == "POST":
#         form = UserChangeForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = UserChangeForm(instance=request.user)
#         args = {'form':form} 
#         return render(request, 'core/profile.html', args)

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


