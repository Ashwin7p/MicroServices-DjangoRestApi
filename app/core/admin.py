"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name']
    readonly_fields = ['last_login']

admin.site.register(models.User, UserAdmin) # for defining the custom fields(using UserAdmin) to be displayed
