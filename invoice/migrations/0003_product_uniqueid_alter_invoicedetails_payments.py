# Generated by Django 4.1.1 on 2022-10-03 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_remove_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='uniqueId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='invoicedetails',
            name='Payments',
            field=models.CharField(choices=[('Airtel_Money', 'Airtel_Money'), ('Mpamba', 'Mpamba'), ('Credit_Card', 'Credit_Card')], max_length=100),
        ),
    ]
