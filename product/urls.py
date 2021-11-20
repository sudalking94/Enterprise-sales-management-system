from django.urls import path
from .views import (ProductListView,
                    SalesListView,
                    ProductCreateView,
                    SaleCreateView,
                    ProductDetailView,
                    ProductUpdateView,
                    SalesDetailView,
                    SalesUpdateView,
                    delete_product,
                    delete_sales)

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('sales/', SalesListView.as_view(), name='sale-list'),
    path('sales/create', SaleCreateView.as_view(), name='sale-create'),
    path('sales/<int:id>/delete', delete_sales, name='delete-sales'),
    path('sales/<int:pk>/edit', SalesUpdateView.as_view(), name='edit-sales'),
    path('sales/<int:pk>/', SalesDetailView.as_view(), name='detail-sales'),
    path('<int:id>/delete/', delete_product, name='delete-product'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='edit-product'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail-product'),
]
