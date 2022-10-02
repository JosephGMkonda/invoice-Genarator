from django.shortcuts import redirect, render,get_object_or_404
from django.template import loader
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from uuid import uuid4
from .models import Product,InvoiceDetails
from .form import addProductForms,addInvoiceForms
from django.contrib import messages


# Create your views here.


def Home(request):
    return render(request, 'invoice/index.html')


def InvoiceView(request):
    context = {}
    invoices = InvoiceDetails.objects.all()
    context['invoices'] = invoices
    return render(request, 'invoice/invoice.html')

def ProductView(request):
    context = {}
    product = Product.objects.all()
    context ['product'] = product

    return render(request, 'invoice/product.html')

    # this view is for creating invoices 
    # creating blank invoice with Invoice number and Transaction Id for the invoice

def createInvoice(request):
    number = "INVOICE-"+str(uuid4()).split('-')[4]
    TransactionId = str(uuid4()).split('-')[4]
    Invoice = InvoiceDetails.objects.create(number=number,TransactionId=TransactionId)
    Invoice.save()

    create_invoice = InvoiceDetails.objects.create(number=number,TransactionId=TransactionId)

    return redirect('build_invoice', slug=create_invoice.slug)




def biuldInvoice(request, slug):

    try:
        getInvoice = InvoiceDetails.objects.get(slug=slug)
    except:
        messages.error(request, "Something went wrong")
        return redirect("invoices")



    products = Product.objects.filter(invoice=getInvoice)

    context = {}
    context ['getInvoice'] = getInvoice
    context['products'] = products

    if request.method == "GET":
        productForm = addProductForms()
        invoiceForm = addInvoiceForms(instance=getInvoice)

        context['productForm'] = productForm
        context['invoiceForm'] = invoiceForm

        return render(request, 'invoice/add_invoice.html',context)
    
    if request.method == "POST":
        productForm = addProductForms(request.POST)
        invoiceForm = addInvoiceForms(request.POST,instance=getInvoice)

        if productForm.is_valid():
            obj = productForm.save(commit=False)
            obj.getInvoice = getInvoice
            obj.save()

            messages.success(request, "The product added succefully")
            return redirect('build_invoice', slug=slug)
        else:
            context['productForm'] = productForm
            context['invoiceForm'] = invoiceForm

            messages.error(request,'Problem when processing your request')
            return render(request, 'invoice/add_invoice.html',context)



    return render(request, 'invoice/add_invoice.html',context)

    




# def productView(request):

#     context = {}
#     product = Product.objects.all()
#     context['product'] = product

#     if request.method == "GET":
#         form = addProductForms()
#         context['form'] = form

#         return render(request,'invoice/product.html')

#     if request.method == "POST":
#         form = addProductForms()

#         if form.is_valid():
#             form = addProductForms(request.POST)
#             form.save()
#             return redirect('products')
#         return render(request, 'invoice/product.html')

# def addProduct(request):
    
#     data = dict()
#     if request.method == "POST":
#         form = addProductForms(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             description = form.cleaned_data.get('description')
#             quantity = form.cleaned_data.get('quantity')
#             prince = form.cleaned_data.get('prince')
#             Currency = form.cleaned_data.get('Currency')
#             ordernumber = form.cleaned_data.get('ordernumber')
#             order_date = form.cleaned_data.get('order_date')

#             p, created = Product.objects.get_or_create(title=title,description=description,quantity=quantity,prince=prince,Currency=Currency,ordernumber=ordernumber,order_date=order_date)
#             print(p)
#             p.save()
#             return redirect('products')
    

#     else:
#         form = addProductForms()

#     context = {
#         'form':form
#     }
#     return render(request, 'invoice/addProduct.html',context)

