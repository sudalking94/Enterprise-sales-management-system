from django.contrib import admin
from . import models


@admin.register(models.Customer)
class Customer(admin.ModelAdmin):
    list_display = (
        "name",
        "enterprise",
        "group",
    )

    list_filter = (
        "enterprise",
    )


@admin.register(models.Group)
class Group(admin.ModelAdmin):

    list_filter = (
        "enterprise",
    )

    list_display = (
        "name",
        "enterprise",
    )
