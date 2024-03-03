"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin): #overriding default super user
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name']
    readonly_fields = ['last_login']
    # (<title>: fields)
    fieldsets = (
        (None, {'fields': ('email', 'password')}), #here None is title
        (_('Personal Info'), {'fields': ('name',)}), #personal info title
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )

admin.site.register(models.User, UserAdmin) # for defining the custom fields(using UserAdmin) to be displayed
