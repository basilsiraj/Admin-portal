from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('admin/', views.admin_view, name='admin'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customer/create/', views.customer_create, name='customer_create'),
    path('customer/edit/<int:id>/', views.customer_edit, name='customer_edit'),
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoice/create/', views.invoice_create, name='invoice_create'),
    path('invoice/edit/<int:id>/', views.invoice_edit, name='invoice_edit'),
]
