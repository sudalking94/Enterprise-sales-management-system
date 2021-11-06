from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from core import managers as core_managers


@admin.register(models.Enterprise)
class Enterprise(UserAdmin):
    model = models.Enterprise

    list_filter = ('name', 'is_staff', 'is_active',)

    fieldsets = (
        (None, {'fields': ('name', 'password')}),
        ('Personal info', {'fields': ('b_no',)}),
        ('Permissions', {'fields': ('is_staff',
         'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'b_no', 'password1', 'password2')}
         ),
    )

    list_display = (
        "name",
        "b_no",
        "is_active",
        "is_staff",
        "is_superuser",
    )

    ordering = ('name',)


@admin.register(models.EnterpriseAccessLog)
class EnterpriseAccessLog(admin.ModelAdmin):

    list_filter = ('enterprise',)
    list_display = (
        "enterprise",
        "os",
        "browser",
        "ip",
        "created",
        "updated"
    )

    fieldsets = (
        (None, {'fields': ('enterprise', 'os',
         'browser', 'ip',)}),
    )
