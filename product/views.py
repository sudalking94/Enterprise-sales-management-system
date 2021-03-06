from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse, redirect, render
from django.http import HttpResponse, Http404
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, SalesLog
from .forms import ProductModelForm, SaleModelForm, ProductUpdateModelForm, SalesUpdateModelForm, SearchForm, SearchSalesLogForm


class ProductListView(LoginRequiredMixin, ListView):
    login_url = "/"

    paginate_by = 10
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['th'] = ["제품 이름", "메모", "가격", "등록 일자"]
        context['create_url'] = reverse("products:product-create")
        context['form'] = SearchForm()
        return context

    def get_queryset(self):
        filters = {}
        if self.request.GET:
            for key, value in self.request.GET.items():
                if key == 'name' and value:
                    key = 'name__icontains'
                    filters[key] = value
        return Product.objects.filter(enterprise=self.request.user, **filters).order_by("-created")


class SalesListView(LoginRequiredMixin, ListView):
    login_url = "/"
    template_name = "sales/sale_list.html"

    paginate_by = 10
    context_object_name = "sales"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['th'] = ["제품 이름", '메모', "구매자", "가격", "결제방식", "구매 일자"]
        context['create_url'] = reverse("products:sale-create")
        context['form'] = SearchSalesLogForm(request=self.request)
        return context

    def get_queryset(self):
        filters = dict()
        if self.request.GET:
            for key, value in self.request.GET.items():
                if key in ['product', 'customer', 'pay_way']:
                    if value:
                        if key == 'product':
                            key = 'product__icontains'
                        elif key == 'customer':
                            key = 'customer__icontains'
                        filters[key] = value
        return SalesLog.objects.filter(enterprise=self.request.user, **filters).order_by("-created")


class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = "product/product_create.html"
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


class ProductDetailView(LoginRequiredMixin, DetailView):
    """ 제품 상세보기 뷰 """

    model = Product

    def get_template_names(self):
        if self.request.htmx:
            return 'product/product_detail_info.html'
        return super().get_template_names()


class SalesDetailView(LoginRequiredMixin, DetailView):
    """ 판매기록 상세보기 뷰 """

    template_name = "sales/sale_detail.html"
    model = SalesLog

    def get_template_names(self):
        if self.request.htmx:
            return 'sales/sales_detail_info.html'
        return super().get_template_names()


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """ 제품 수정 """

    template_name = "partials/edit_form.html"
    model = Product
    form_class = ProductUpdateModelForm


class SalesUpdateView(LoginRequiredMixin, UpdateView):
    """ 판매기록 수정 """

    template_name = "partials/edit_form.html"
    model = SalesLog
    form_class = SalesUpdateModelForm


@login_required
def delete_product(request, id=None):
    try:
        obj = Product.objects.get(id=id, enterprise=request.user)
    except Product.DoesNotExist:
        obj = None
    if obj is None:
        if request.htmx:
            return HttpResponse("Not Found")
        raise Http404
    if request.method == 'DELETE' and request.htmx:
        obj.delete()
        url = reverse('products:product-list')
        headers = {
            'HX-Redirect': url
        }
        return HttpResponse("Success", headers=headers)
    return redirect('/')


@login_required
def delete_sales(request, id=None):
    try:
        obj = SalesLog.objects.get(id=id, enterprise=request.user)
    except SalesLog.DoesNotExist:
        obj = None
    if obj is None:
        if request.htmx:
            return HttpResponse("Not Found")
        raise Http404
    if request.method == 'DELETE' and request.htmx:
        obj.delete()
        url = reverse('products:sale-list')
        headers = {
            'HX-Redirect': url
        }
        return HttpResponse("Success", headers=headers)
    return redirect('/')
