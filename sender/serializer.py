from rest_framework import serializers
from .models import *


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailModel
        fields = '__all__'