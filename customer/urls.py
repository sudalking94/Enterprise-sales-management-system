from django.urls import path
from .views import CustomerListView, CustomerCreateView, GroupCreateView, CustomerDetailView, CustomerUpdateView, delete_customer

app_name = 'customers'

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer-list'),
    path('create', CustomerCreateView.as_view(), name='customer-create'),
    path('group/create', GroupCreateView.as_view(), name='create-group'),
    path('<int:id>/delete/', delete_customer, name="delete-customer"),
    path('<int:pk>/edit/', CustomerUpdateView.as_view(), name="edit-customer"),
    path('<int:pk>/', CustomerDetailView.as_view(), name="detail-customer"),
]
