# Generated by Django 4.0.4 on 2022-05-31 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smile', '0014_rename_locationmarkup_product_ploc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pSalePrice',
        ),
    ]