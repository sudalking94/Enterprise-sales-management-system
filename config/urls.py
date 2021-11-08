from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from customer.views import LandingPageView, DashboardView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
