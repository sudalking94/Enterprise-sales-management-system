from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, SalesLog


class ProductListView(LoginRequiredMixin, ListView):
    login_url = "/"
    template_name = "products/product_list.html"

    paginate_by = 10
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter(enterprise=self.request.user).order_by("-created")


class SalesListView(LoginRequiredMixin, ListView):
    login_url = "/"
    template_name = "sales/sale_list.html"

    paginate_by = 10
    context_object_name = "sales"

    def get_queryset(self):
        return SalesLog.objects.filter(enterprise=self.request.user).order_by("-created")
