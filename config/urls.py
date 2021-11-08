from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from customer.views import LandingPageView, DashboardView
from enterprise.views import SignupView
from enterprise.forms import LoginFormView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('customers/', include('customer.urls', namespace='customers')),
    path('products/', include('product.urls', namespace='products')),
    path('signup/', SignupView.as_view(), name='signup'),
]
