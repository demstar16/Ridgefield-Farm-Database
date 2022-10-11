from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User


class AccessRequestForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'role', 'email', 'password1', 'password2', )
