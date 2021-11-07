from django.contrib import admin
from . import models


@admin.register(models.Product)
class Product(admin.ModelAdmin):

    list_display = (
        "name",
        "won_price",
        "created",
        "updated",
    )


@admin.register(models.SalesLog)
class SalesLog(admin.ModelAdmin):

    list_display = (
        "product",
        "enterprise",
        "customer",
        "pay_way",
        "created",
    )
