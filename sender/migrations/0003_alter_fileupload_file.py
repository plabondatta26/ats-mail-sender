# Generated by Django 3.2.9 on 2021-11-26 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sender', '0002_auto_20211126_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='file',
            field=models.FileField(upload_to='files/'),
        ),
    ]