# Generated by Django 3.1.7 on 2021-04-03 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_remove_userprofile_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='toa',
        ),
    ]
