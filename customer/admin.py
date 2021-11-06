from django.contrib import admin
from . import models


@admin.register(models.Customer)
class Customer(admin.ModelAdmin):
    list_display = (
        "name",
        "enterprise",
        "group",
    )


@admin.register(models.Group)
class Group(admin.ModelAdmin):
    list_display = (
        "name",
        "enterprise",
    )
