from django.urls import path
from . import views


urlpatterns = [

    path('', views.Home, name="home"),
    path("invoices", views.InvoiceView, name='invoices'),
    path('invoices/create',views.createInvoice, name='create-invoice'),
    
    path('invoices/create-build/<slug:slug>', views.biuldInvoice, name='build_invoice')
    
]