from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from src.users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    """Управление пользователями."""

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('role', 'email', 'first_name',
                                         'last_name', 'bio')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {'fields': ('role', 'username', 'password1', 'password2')}),
        (_('Personal info'), {'fields': ('email', 'first_name', 'last_name')})
    )
    list_display = (
        'id', 'username', 'role', 'first_name', 'last_name', 'email')
    list_display_links = ('username',)
    search_fields = ('username', 'email', 'first_name', 'last_name')
    save_on_top = True
