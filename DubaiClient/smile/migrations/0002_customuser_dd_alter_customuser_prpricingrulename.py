# Generated by Django 4.0.4 on 2022-05-28 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='dd',
            field=models.ForeignKey(db_column='dd', default='All', on_delete=django.db.models.deletion.DO_NOTHING, to='smile.pricingrule', to_field='prPricingRuleName'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='prPricingRuleName',
            field=models.CharField(max_length=300),
        ),
    ]
