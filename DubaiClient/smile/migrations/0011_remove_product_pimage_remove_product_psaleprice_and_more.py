# Generated by Django 4.0.4 on 2022-05-31 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smile', '0010_remove_productpricinglist_categorymarkup_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pImage',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pSalePrice',
        ),
        migrations.AddField(
            model_name='productpricinglist',
            name='categoryMarkUp',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='smile.category'),
        ),
        migrations.AddField(
            model_name='productpricinglist',
            name='locationMarkUp',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='smile.location'),
        ),
        migrations.AddField(
            model_name='productpricinglist',
            name='priceMarkup',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='smile.product'),
        ),
        migrations.AddField(
            model_name='productpricinglist',
            name='usernameID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]
