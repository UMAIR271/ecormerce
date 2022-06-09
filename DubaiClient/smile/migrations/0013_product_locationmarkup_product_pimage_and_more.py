# Generated by Django 4.0.4 on 2022-05-31 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smile', '0012_product_psaleprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='locationMarkUp',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='smile.location'),
        ),
        migrations.AddField(
            model_name='product',
            name='pImage',
            field=models.ImageField(default='', upload_to='smile/images/productImages'),
        ),
        migrations.AddField(
            model_name='product',
            name='usernameID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]
