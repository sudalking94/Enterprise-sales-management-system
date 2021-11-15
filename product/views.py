from django.shortcuts import reverse
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, SalesLog
from .forms import ProductModelForm, SaleModelForm


class ProductListView(LoginRequiredMixin, ListView):
    login_url = "/"
    template_name = "products/product_list.html"

    paginate_by = 10
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['th'] = ["제품 이름", "소속 기업", "가격", "등록 일짜"]
        context['create_url'] = reverse("products:product-create")
        return context

    def get_queryset(self):
        return Product.objects.filter(enterprise=self.request.user).order_by("-created")


class SalesListView(LoginRequiredMixin, ListView):
    login_url = "/"
    template_name = "sales/sale_list.html"

    paginate_by = 10
    context_object_name = "sales"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['th'] = ["제품 이름", "구매자", "가격", "결제방식", "구매 일짜"]
        context['create_url'] = reverse("products:sale-create")
        return context

    def get_queryset(self):
        return SalesLog.objects.filter(enterprise=self.request.user).order_by("-created")


class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = "products/product_create.html"
    form_class = ProductModelForm

    def get_success_url(self):
        return reverse("products:product-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class SaleCreateView(LoginRequiredMixin, CreateView):
    template_name = "sales/sale_create.html"
    form_class = SaleModelForm

    def get_success_url(self):
        return reverse("products:sale-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
