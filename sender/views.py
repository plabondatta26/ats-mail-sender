from django.shortcuts import render, redirect
from .forms import *
import pandas as pd
from django.conf import settings
from rest_framework.generics import ListAPIView
from .serializer import *


# Create your views here.

def home(request):
    return render(request, 'index.html')


def save_emails(data, user_id):
    for i in data['email']:
        x = i.split(':')
        if x[0] == 'mailto':
            EmailModel.objects.create(user_id=user_id, email=x[1])
        else:
            EmailModel.objects.create(user_id=user_id, email=x[0])
    return None


def save_file_data(request):
    if request.method == 'POST':
        user_id = request.user.id
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data = FileUpload.objects.filter(user=user_id).latest('created_at')
            ext = data.file.name.split('.')[-1]
            if ext == 'csv':
                df = pd.read_csv(str(settings.BASE_DIR) + data.file.url)
                save_emails(df, user_id)
            elif ext == 'xlsx':
                df = pd.read_excel(str(settings.BASE_DIR) + data.file.url)
                save_emails(df, user_id)
            return redirect('/')
        return redirect('/')


class LoadEmail(ListAPIView):
    serializer_class = EmailSerializer

    def get_queryset(self):
        queryset = EmailModel.objects.all()
        return queryset.filter(user=self.request.user)

