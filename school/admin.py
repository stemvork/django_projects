from django.contrib import admin
from django.db.models.functions import Lower
from decorator import decorator
from .models import *

common_kwargs = {
    "list_display": ['active', 'name'],
    "list_display_links": ['name'],
    "list_editable": ['active'],
    "ordering": ['name'],
}

class CommonModelAdmin(admin.ModelAdmin):
    list_display = ['active','name']
    list_display_links = ['name']
    list_editabel = ['active']
    ordering = ['name']

@admin.register(Hour)
class HourAdmin(CommonModelAdmin):
    list_display = ['active', 'name', 'start_time', 'end_time']

@admin.register(Classroom)
class ClassroomAdmin(CommonModelAdmin):
    pass

@admin.register(Subject)
class SubjectAdmin(CommonModelAdmin):
    pass

@admin.register(Publisher)
class PublisherAdmin(CommonModelAdmin):
    pass

admin.site.register(MaterialList)

@admin.register(Book)
class BookAdmin(CommonModelAdmin):
    pass

@admin.register(Practical)
class PracticalAdmin(CommonModelAdmin):
    list_display = ['active', 'name', 'book']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['active', 'user', 'first_name', 'subjects']
    list_display_links = ['user']
    def is_active(self, request):
        print(self)
    ordering = ['user__username']


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.models import User
from .models import UserProfile

class ProfileInline(admin.StackedInline):
    model = UserProfile
    fk_name = 'user'
    can_delete = False
    max_num = 1

class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline, ]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
