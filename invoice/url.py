from django.urls import path
from . import views


urlpatterns = [

    path('', views.InvoiceView, name="invoices"),
    path('products', views.ProductView, name="products"),
    path('invoices/create',views.createInvoice, name='create-invoice'),
    path('invoices/create-build/<slug:slug>', views.biuldInvoice, name='build_invoice'),
    path('invoices/view-pdf/<slug:slug>',views.viewPDFInvoic, name='view-pdf-invoice'),
    path('invoices/view-document/<slug:slug>',views.viewDocumentInvoice, name='view-document-invoice'),
    
]