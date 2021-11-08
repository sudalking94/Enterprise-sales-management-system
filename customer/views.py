from django.views.generic import TemplateView, ListView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Customer


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

    def get_queryset(self):
        return Customer.objects.filter(enterprise=self.request.user).order_by("-created")
