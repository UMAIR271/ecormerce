# Generated by Django 4.0.4 on 2022-06-01 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smile', '0024_alter_customuser_ploc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='pLoc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='smile.location'),
        ),
    ]
