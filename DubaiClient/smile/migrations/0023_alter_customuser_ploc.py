# Generated by Django 4.0.4 on 2022-05-31 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smile', '0022_alter_customuser_ploc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='pLoc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='smile.location'),
        ),
    ]
