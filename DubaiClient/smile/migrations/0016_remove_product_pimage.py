# Generated by Django 4.0.4 on 2022-05-31 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smile', '0015_remove_product_psaleprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pImage',
        ),
    ]
