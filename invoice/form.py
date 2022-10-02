
from django import forms
from .models import Product,InvoiceDetails

class DateInput(forms.DateInput):
    input_type = 'date'


class addInvoiceForms(forms.ModelForm):

    PAYMENT_CHOICE = {
        ('Credit_Card','Credit_Card'),
        ('Airtel_Money','Airtel_Money'),
        ('Mpamba','Mpamba')
        
    }

    title = forms.CharField(widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}))
    number = forms.IntegerField(widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}))
    TransactionId = forms.IntegerField(widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}))
    Payments = forms.ChoiceField(choices=PAYMENT_CHOICE)
    

    class Meta:
        model = InvoiceDetails
        fields = ['title','number','TransactionId','Payments','order']
        widgets = {
            'order': DateInput(),
        }



class addProductForms(forms.ModelForm):

    CURRENCY = {
        ("k","kwacha"),
        ("$","USD")
    }

    title = forms.CharField(widget=forms.TextInput, required=True)
    description = forms.CharField(widget=forms.Textarea,required=False)
    quantity = forms.IntegerField(widget=forms.TextInput, required=True)
    prince = forms.FloatField(widget=forms.TextInput, required=True)
    Currency = forms.ChoiceField(choices=CURRENCY, required=True)
    ordernumber = forms.IntegerField(widget=forms.TextInput, required=True)
    


    class Meta:
        model = Product
        fields = ['title','description','quantity','prince','Currency','ordernumber','order_date']
        widgets = {
            'order_date': DateInput(),
        }



