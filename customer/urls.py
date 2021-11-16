from django.urls import path
from .views import CustomerListView, CustomerCreateView, delete_customer

app_name = 'customers'

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer-list'),
    path('create', CustomerCreateView.as_view(), name='customer-create'),
    path('<int:id>/delete/', delete_customer, name="delete-customer"),
]
