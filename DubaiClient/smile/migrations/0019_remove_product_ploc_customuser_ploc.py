# Generated by Django 4.0.4 on 2022-05-31 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smile', '0018_productpricinglist_pname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pLoc',
        ),
        migrations.AddField(
            model_name='customuser',
            name='pLoc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='smile.location'),
        ),
    ]
