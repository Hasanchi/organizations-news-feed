from django.contrib import admin

from .models import Organizations, Employee, Post, Dvision


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['group', 'user', 'status']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title',  'author', 'publish', 'status']

@admin.register(Dvision)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Organizations)
class OrganizationsAdmin(admin.ModelAdmin):
    list_display = ['name']
