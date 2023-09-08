from django.contrib import admin

from .models import Organizations, Employee, Post, Dvision


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['group', 'user', 'status']

