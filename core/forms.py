from socket import fromshare
from django import forms
from accounts.models import User

class BioForm(forms.ModelForm):
    body = forms.CharField(required=True,
    widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Dweet something...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",)
    
    class Meta:
        model = User
        exclude = ("id",'email','role','is_active',
        'create_time',"password",'last_login',"group","username","first_name","last_name",
        "date_joined","groups","id_is_staff","user_permissions","is_superuser",
        "is_staff","bio",)