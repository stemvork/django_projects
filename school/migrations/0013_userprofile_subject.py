# Generated by Django 3.1.7 on 2021-04-03 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_remove_userprofile_toa'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='subject',
            field=models.ManyToManyField(to='school.Subject'),
        ),
    ]
