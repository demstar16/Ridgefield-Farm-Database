from django import forms
from accounts.models import User

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('bio',)


        