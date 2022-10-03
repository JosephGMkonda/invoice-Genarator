
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
    Payments = forms.ChoiceField(choices=PAYMENT_CHOICE)
    

    class Meta:
        model = InvoiceDetails
        fields = ['title','Payments','order']
        widgets = {
            'order': DateInput(),
        }



class addProductForms(forms.ModelForm):

    CURRENCY = {
        ("k","kwacha"),
        ("$","USD")
    }

    title = forms.CharField(widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}), required=True)
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}), required=True)
    prince = forms.FloatField(widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}), required=True)
    Currency = forms.ChoiceField(choices=CURRENCY,required=True)
   
    


    class Meta:
        model = Product
        fields = ['title','quantity','prince','Currency','order_date']
        widgets = {
            'order_date': DateInput(),
        }



