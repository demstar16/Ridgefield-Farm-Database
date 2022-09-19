from django.shortcuts import render, redirect
from .forms import FileForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from .models import File

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
    return render(request, 'files/upload.html', context)


@login_required(login_url='accounts/login')
def viewFile(request, pk):
    file_info = File.objects.get(id=pk)
    context = {'file': file_info}
    return render(request, 'files/file.html', context)