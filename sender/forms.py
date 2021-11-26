from django import forms
from .models import *


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = '__all__'
