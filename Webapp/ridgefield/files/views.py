from code import interact
from django.core import management
from django.shortcuts import render, redirect
from .forms import FileForm, FileEditForm, FileUpdateForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from .models import File, Tag, Paddock, PastFile
from core.views import browse


# Create your views here.
@login_required(login_url='accounts/login')
def upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.uploader = request.user
            upload.name = upload.filedata.name
            upload.save()
            return redirect('file', upload.id)
    else:
        form = FileForm()
    context = {'form': form}
    return render(request, 'upload.html', context)


@login_required(login_url='accounts/login')
def viewFile(request, pk):
    file_info = File.objects.get(id=pk)
    form = FileUpdateForm()
    context = {'file': file_info, 'past_versions':file_info.past_versions, 'form': form}
    return render(request, 'file.html', context)

@login_required(login_url='accounts/login')
def delete_confirm(request, pk):
    file_info = File.objects.get(id=pk)
    context =  {'file': file_info}
    return render(request, "delete.html", context)

@login_required(login_url='accounts/login')
def deleteAllConfirm(request):
    
    return render(request, "delete_all.html")

@login_required(login_url='accounts/login')
def file_delete(request, pk):
    file = File.objects.get(id=pk)
    if request.user.id == file.uploader.id:
        file.deleted = 1
        file.save()
    return redirect('browse')

@login_required(login_url='accounts/login')
def fileRestore(request, pk):
    file = File.objects.get(id=pk)
    file.deleted = 0
    file.save()
    return redirect('browse')

@login_required(login_url='accounts/login')
def permanentDelete(request, pk):
    file = File.objects.get(id=pk)
    file.delete()
    return redirect('browse')

@login_required(login_url='accounts/login')
def cleanDatabase(request):
    management.call_command('cleanup_unused_media', interactive=False)
    return redirect('browse')

@login_required(login_url='accounts/login')
def permenantDeleteAll(request):
    files = File.objects.all().filter(deleted=1)
    for file in files:
        file.delete()
    return redirect('browse')

@login_required(login_url='accounts/login')
def edit(request, pk):
    if request.method == 'POST':
        form = FileEditForm(request.POST, request.FILES)
        if form.is_valid():
            edited = File.objects.get(id=pk)
            edited.name = form.data['name']
            edited.description = form.data['description']
            tag = Tag.objects.get(id=form.data['tags'])
            edited.tags = tag
            paddock = Paddock.objects.get(id=form.data['paddocks'])
            edited.paddocks = paddock
            edited.save()
            
            return redirect('file', pk=edited.id)
    else:
        file = File.objects.get(id=pk)
        form = FileEditForm(initial = {
            'name': file.name,
            'tags': file.tags,
            'paddocks': file.paddocks,
            'description': file.description
        })
    context = {'form': form}
    return render(request, 'edit.html', context)

@login_required(login_url='accounts/login')
def update(request, pk):
    if request.method == 'POST':
        form = FileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            updated = File.objects.get(id=pk)
            backup = PastFile(filedata=updated.filedata, user=request.user, fileref=updated)
            backup.save()
            updated.filedata = file.filedata
            updated.name = file.filedata.name
            updated.save()
            return redirect('file', pk=updated.id)
    else:
        form = FileUpdateForm()
    context = {'form': form}
    return render(request, 'update.html', context)