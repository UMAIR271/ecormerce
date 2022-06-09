# Generated by Django 4.0.4 on 2022-05-31 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('smile', '0008_remove_customuser_dd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('lID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('lName', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='productpricinglist',
            name='productPrice',
        ),
        migrations.AddField(
            model_name='productpricinglist',
            name='categoryMarkUp',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='smile.category'),
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
        migrations.AddField(
            model_name='productpricinglist',
            name='locationMarkUp',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='smile.location'),
        ),
    ]