from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from perfis.forms import *


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('matricula', 'nome', 'sobrenome', 'is_admin')
    list_filter = ('is_admin', 'matricula', 'nome')
    fieldsets = (
        (None, {'fields': ('matricula', 'password')}),
        ('Dados Pessoais', {'fields': ('nome', 'sobrenome')}),
        ('Permissões', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('matricula', 'nome', 'sobrenome', 'password1', 'password2')
        }),
    )
    search_fields = ('matricula', 'nome')
    ordering = ('matricula',)
    filter_horizontal = ()


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
