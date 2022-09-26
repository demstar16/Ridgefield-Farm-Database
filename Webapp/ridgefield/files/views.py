
from django.shortcuts import render, redirect
from .forms import FileForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from .models import File
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
            return redirect('index')
    else:
        form = FileForm()
    context = {'form': form}
    return render(request, 'upload.html', context)


@login_required(login_url='accounts/login')
def viewFile(request, pk):
    file_info = File.objects.get(id=pk)
    context = {'file': file_info}
    return render(request, 'file.html', context)

@login_required(login_url='accounts/login')
def delete_confirm(request, pk):
    file_info = File.objects.get(id=pk)
    context =  {'file': file_info}
    return render(request, "delete.html", context)

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

