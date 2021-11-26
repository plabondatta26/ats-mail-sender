from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class FileUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(blank=False, upload_to='files/')
    created_at = models.DateTimeField(auto_now_add=True)


class EmailModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' / ' + self.email


class EmailSettings(models.Model):
    host = models.CharField(max_length=100, blank=False, null=False)
    port = models.CharField(max_length=5, blank=False, null=False)
    password = models.CharField(max_length=5, blank=False, null=False)
    ssl = models.BooleanField(default=True)


class MailLimit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    limit = models.CharField(max_length=100, blank=False, null=False)
    used = models.CharField(max_length=100, blank=False, null=False)
    available = models.CharField(max_length=100, blank=False, null=False)


class SendMail(models.Model):
    subject = models.CharField(max_length=200, blank=False, null=False)
    message = models.TextField(max_length=1000, blank=False, null=False)

