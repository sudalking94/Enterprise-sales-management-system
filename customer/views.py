from django.views.generic import TemplateView, ListView, CreateView
from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Customer
from .forms import CustomerModelForm


class LandingPageView(TemplateView):
    template_name = "landing.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard")
        return super().dispatch(request, *args, **kwargs)


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = "/"
    template_name = "dashboard.html"


class CustomerListView(LoginRequiredMixin, ListView):
    login_url = "/"
    template_name = "customers/customer_list.html"

    paginate_by = 10
    context_object_name = "customers"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['th'] = ["이름", "소속 기업", "성별", "소속 그룹", "메모", "등록 일짜"]
        context['create_url'] = reverse("customers:customer-create")
        return context

    def get_queryset(self):
        return Customer.objects.filter(enterprise=self.request.user).order_by("-created")


class CustomerCreateView(LoginRequiredMixin, CreateView):
    template_name = "customers/customer_create.html"
    form_class = CustomerModelForm

    def get_success_url(self):
        return reverse("customers:customer-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
