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
