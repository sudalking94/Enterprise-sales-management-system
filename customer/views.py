from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect


class LandingPageView(TemplateView):
    template_name = "landing.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard")
        return super().dispatch(request, *args, **kwargs)


class DashboardView(TemplateView):
    template_name = "dashboard.html"
