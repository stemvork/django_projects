# Generated by Django 3.1.7 on 2021-04-03 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20210403_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
