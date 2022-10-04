from django import forms
from .models import File, Tag

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('filedata','tags', 'description', 'paddocks')


class FileEditForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('name', 'tags', 'description', 'paddocks')

class FileUpdateForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('filedata',)

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)