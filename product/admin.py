from django.contrib import admin
from . import models


@admin.register(models.Product)
class Product(admin.ModelAdmin):

    list_filter = ('enterprise',)

    list_display = (
        "name",
        "enterprise",
        "won_price",
        "created",
        "updated",
    )


@admin.register(models.SalesLog)
class SalesLog(admin.ModelAdmin):

    list_filter = ('enterprise',)

    list_display = (
        "product",
        "enterprise",
        "won_price",
        "customer",
        "pay_way",
        "created",
    )
