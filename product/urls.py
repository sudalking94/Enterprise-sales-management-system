from django.urls import path
from .views import ProductListView, SalesListView, ProductCreateView, SaleCreateView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('sales/', SalesListView.as_view(), name='sale-list'),
    path('sales/create', SaleCreateView.as_view(), name='sale-create'),
]
