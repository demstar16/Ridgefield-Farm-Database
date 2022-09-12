from django.shortcuts import render
from django.contrib.auth import login, authenticate
from accounts.forms import AccessRequestForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = AccessRequestForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'registration/request_sent.html')
    else:
        form = AccessRequestForm()
    return render(request, 'registration/register.html', {'form': form})