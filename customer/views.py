from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.shortcuts import redirect
from .models import Customer


class LandingPageView(TemplateView):
    template_name = "landing.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard")
        return super().dispatch(request, *args, **kwargs)


class DashboardView(TemplateView):
    template_name = "dashboard.html"


class CustomerListView(ListView):
    template_name = "customers/customer_list.html"

    model = Customer
    paginate_by = 10
    ordering = "-created"
    context_object_name = "customers"
