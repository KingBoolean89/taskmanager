from django.contrib import admin
from task.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','created_at']

admin.site.register(Task, TaskAdmin)
# Register your models here.
