# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-05 08:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20171005_1126'),
        ('orders', '0002_auto_20171005_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer2',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer2', to='customers.Customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer3',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer3', to='customers.Customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer4',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer4', to='customers.Customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer5',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer5', to='customers.Customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer6',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer6', to='customers.Customer'),
        ),
    ]
