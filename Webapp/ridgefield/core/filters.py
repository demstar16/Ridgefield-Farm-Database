import django_filters

from files.models import *

class FileFilter(django_filters.FilterSet):
    class Meta:
        model = File
        fields = '__all__'