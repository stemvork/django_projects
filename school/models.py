from django.db import models

# Create your models here.

class Hour(models.Model):
    name = models.IntegerField(default=1)
    start_time = models.CharField(max_length=5, default="00:00")
    end_time = models.CharField(max_length=5, default="00:00")
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

class Classroom(models.Model):
    name = models.CharField(max_length=10, default="A01")
    order = models.IntegerField(default=1)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=200, help_text='Please enter a subject name.')
    abbreviation = models.CharField(max_length=3, blank=True, null=True)
    blocked_days = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.RESTRICT, help_text='Please choose the subject.')
    name = models.CharField(max_length=200, help_text='Please enter the book title.')
    publisher = models.ForeignKey(Publisher, on_delete=models.RESTRICT, null=True)
    remark = models.TextField(max_length=280, help_text='Important notes about this book.', blank=True, null=True)
    order = models.IntegerField(default=1)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Practical(models.Model):
    book   = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=200)
    practical_number = models.CharField(max_length=10, null=True, blank=True)
    paragraph_number = models.CharField(max_length=10, null=True, blank=True)
    theorybook_page = models.CharField(max_length=10, null=True, blank=True)
    workbook_page = models.CharField(max_length=10, null=True, blank=True)
    task_load = models.IntegerField(null=True, blank=True)
    order = models.IntegerField(default=1, null=True, blank=True)
    url = models.TextField(max_length=1000, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('practical-detail', args=[str(self.id)])

class MaterialList(models.Model):
    practical = models.ForeignKey(Practical, on_delete=models.CASCADE, null=True)

from django.contrib.auth.models import User
from django.db.models.signals import post_save
class UserProfile(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    subject    = models.ManyToManyField(Subject)
    
    def active(self):
        return self.user.is_active
    active.boolean = True
    
    def first_name(self):
        return self.user.first_name

    def subjects(self):
        return ', '.join(map(str, self.subject.all()))

    def __str__(self):
        return self.user.username

# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         profile = UserProfile()
#         profile.user = instance
#         profile.save()
# 
# post_save.connect(create_user_profile, sender=User)

