from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
from uuid import uuid4




class InvoiceDetails(models.Model):
    

    PAYMENT_CHOICE = {
        ('Credit_Card','Credit_Card'),
        ('Airtel_Money','Airtel_Money'),
        ('Mpamba','Mpamba')
        
    }
    title = models.CharField(null=True, blank=True,max_length = 100)
    number = models.CharField(max_length = 100,null=True, blank=True)
    TransactionId = models.CharField(max_length = 100,null=True, blank=True)
    Payments = models.CharField(choices=PAYMENT_CHOICE, max_length=100)
    order = models.DateField(null=True, blank=True)
    

    # related Field

    owner = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,)
    

    
    # utility id 
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    

    def __str__(self):
        return '{} {}'.format(self.number, self.uniqueId)


    def get_absolute_url(self):
        return reverse('invoice-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.order is None:
            self.order = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.number, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.number, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(InvoiceDetails, self).save(*args, **kwargs)


    
    
    
class Product(models.Model):
    CURRENCY = {
        ("k","kwacha"),
        ("$","USD")
    }

    title = models.CharField(null=True, blank=True,max_length = 250)
    quantity = models.IntegerField(null=True, blank=True)
    prince = models.FloatField(null=True, blank=True)
    Currency = models.CharField(choices=CURRENCY,default="K",max_length=100)
    order_date = models.DateField(null=True, blank=True)

    #Related Field
    invoice = models.ForeignKey(InvoiceDetails, blank=True, null=True, on_delete=models.CASCADE)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)

    
    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)


    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.order_date is None:
            self.order_date = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Product, self).save(*args, **kwargs)
    

