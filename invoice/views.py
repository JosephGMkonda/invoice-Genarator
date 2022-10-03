from re import template
from django.shortcuts import redirect, render,get_object_or_404
from django.template import loader
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from uuid import uuid4
from .models import Product,InvoiceDetails
from .form import addProductForms,addInvoiceForms
from django.contrib import messages

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required




# Create your views here.




# getting all invoices
@login_required
def InvoiceView(request):
    context = {}
    invoices = InvoiceDetails.objects.all()
    context['invoices'] = invoices
    return render(request, 'invoice/invoice.html')


    # getting all products including the inviuce which they belong
@login_required
def ProductView(request):
    context = {}
    products = Product.objects.all()
    
    context ['product'] = products

    return render(request, 'invoice/product.html', context)

    # this view is for creating invoices 
    # creating blank invoice with Invoice number and Transaction Id for the invoice
@login_required
def createInvoice(request):
    number = "INVOICE-"+str(uuid4()).split('-')[4]
    TransactionId = str(uuid4()).split('-')[4]
    Invoice = InvoiceDetails.objects.create(number=number,TransactionId=TransactionId)
    Invoice.save()

    create_invoice = InvoiceDetails.objects.create(number=number,TransactionId=TransactionId)

    return redirect('build_invoice', slug=create_invoice.slug)



@login_required
def biuldInvoice(request, slug):

    try:
        getInvoice = InvoiceDetails.objects.get(slug=slug)
    except:
        messages.error(request, "Something went wrong")
        return redirect("invoices")


    # the object get all the product that are related to specific invoice 
    # so that to make it easy to calculate total number of products on specific invoice
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
        elif invoiceForm.is_valid():
            invoiceForm.save()
        else:
            context['productForm'] = productForm
            context['invoiceForm'] = invoiceForm

            messages.error(request,'Problem when processing your request')
            return render(request, 'invoice/add_invoice.html',context)



    return render(request, 'invoice/add_invoice.html',context)

    

# The function caculate total invoices 
@login_required
def viewPDFInvoic(request, slug):

    try:
        invoice = InvoiceDetails.objects.get(slug=slug)
    
    except:
        messages.error(request, 'Something went wrong')
        return redirect('invoices')

    
    products = Product.objects.filter(invoice=invoice)

    
    
    invoiceCurrency = ''
    invoiceTotal = 0.0
    if len(products) > 0:
        for x in products:
            y = float(x.quantity) * float(x.price)
            invoiceTotal += y
            invoiceCurrency = x.currency



    context = {}
    context['invoice'] = invoice
    context['products'] = products
    
    context['invoiceTotal'] = "{:.2f}".format(invoiceTotal)
    context['invoiceCurrency'] = invoiceCurrency

    return render(request, 'invoice/invoice-temp.html', context)
# this function used to generate FDF
@login_required
def viewDocumentInvoice(request, slug):
    
    try:
        invoice = InvoiceDetails.objects.get(slug=slug)
    
    except:
        messages.error(request, 'Something went wrong')
        return redirect('invoices')

    
    products = Product.objects.filter(invoice=invoice)

    
    
    invoiceCurrency = ''
    invoiceTotal = 0.0
    if len(products) > 0:
        for x in products:
            y = float(x.quantity) * float(x.price)
            invoiceTotal += y
            invoiceCurrency = x.currency

    

    context = {}
    context['invoice'] = invoice
    context['products'] = products
    
    context['invoiceTotal'] = "{:.2f}".format(invoiceTotal)
    context['invoiceCurrency'] = invoiceCurrency

    template = get_template("invoice/pdf-temp.html")

    html = template.render(context)

    buf = io.Bytes.IO()
    c = canvas.Canvas(buf,pagesize=letter)
    textob = c.beginText()
    textob.TextLine(html)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse


    




