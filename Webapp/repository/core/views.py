from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import User, Paddock, File
from django.db.models import Q
from .forms import FileForm
from django.core.files.storage import FileSystemStorage

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "core/register.html"

@login_required(login_url='/login')
def index(request):
    paddocks = Paddock.objects.all()
    files = File.objects.all()[0:5]
    context = {'paddocks': paddocks, 'files': files}
    return render(request, 'core/index.html', context)

@login_required(login_url='/login')
def viewProfile(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'core/profile.html', context)

@login_required(login_url='/login')
def viewPaddock(request, pk):
    paddock = Paddock.objects.get(id=pk)
    files = File.objects.filter(paddocks=pk)
    context = {'paddock': paddock, 'files': files}
    return render(request, 'core/paddock.html', context)

@login_required(login_url='/login')
def viewFile(request, pk):
    file_info = File.objects.get(id=pk)
    tags = []
    for tag in file_info.tags.all():
        tags.append(tag)
    context = {'file': file_info, 'tags': tags}
    return render(request, 'core/file.html', context)

@login_required(login_url='/login')
def search(request):
    q = request.GET.get('q')
    files = File.objects.filter(
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    context = {'query': q, 'files': files}
    return render(request, 'core/search.html', context)

@login_required(login_url='/login')
def upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FileForm()
    context = {'form': form}
    return render(request, 'core/upload.html', context)