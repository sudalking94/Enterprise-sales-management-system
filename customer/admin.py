from django.contrib import admin
from . import models


@admin.register(models.Customer)
class Customer(admin.ModelAdmin):
    pass


@admin.register(models.Group)
class Group(admin.ModelAdmin):
    pass
