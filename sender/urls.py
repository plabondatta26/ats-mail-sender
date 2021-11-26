from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('save/file/', save_file_data, name='save_file_data'),
    path('get/emails/', LoadEmail.as_view(), name='LoadEmail')
]

