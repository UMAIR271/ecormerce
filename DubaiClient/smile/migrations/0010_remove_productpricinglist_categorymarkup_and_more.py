# Generated by Django 4.0.4 on 2022-05-31 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smile', '0009_location_remove_productpricinglist_productprice_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpricinglist',
            name='categoryMarkUp',
        ),
        migrations.RemoveField(
            model_name='productpricinglist',
            name='locationMarkUp',
        ),
        migrations.RemoveField(
            model_name='productpricinglist',
            name='priceMarkup',
        ),
        migrations.RemoveField(
            model_name='productpricinglist',
            name='usernameID',
        ),
    ]
