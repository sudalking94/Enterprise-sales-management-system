from django.urls import path
from .views import ProductListView, SalesListView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('sales/', SalesListView.as_view(), name='sale-list'),
]
