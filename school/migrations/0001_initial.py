# Generated by Django 3.1.7 on 2021-04-03 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Please enter the book title.', max_length=200)),
                ('remark', models.TextField(blank=True, help_text='Important notes about this book.', max_length=280, null=True)),
                ('order', models.IntegerField(default=1)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Please enter a subject name.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Practical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('practical_number', models.CharField(blank=True, max_length=10, null=True)),
                ('paragraph_number', models.CharField(blank=True, max_length=10, null=True)),
                ('theorybook_page', models.CharField(blank=True, max_length=10, null=True)),
                ('workbook_page', models.CharField(blank=True, max_length=10, null=True)),
                ('task_load', models.IntegerField(blank=True, null=True)),
                ('order', models.IntegerField(blank=True, default=1, null=True)),
                ('url', models.TextField(blank=True, max_length=1000, null=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.book')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practical', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.practical')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='school.publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='subject',
            field=models.ForeignKey(help_text='Please choose the subject.', on_delete=django.db.models.deletion.RESTRICT, to='school.subject'),
        ),
    ]