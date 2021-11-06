from django.contrib import admin
from . import models


@admin.register(models.Product)
class Product(admin.ModelAdmin):

    list_display = (
        "name",
        "price",
        "created",
        "updated",
    )


@admin.register(models.SalesLog)
class SalesLog(admin.ModelAdmin):

    list_display = (
        "enterprise",
        "customer",
        "product",
        "pay_way",
        "created",
    )
