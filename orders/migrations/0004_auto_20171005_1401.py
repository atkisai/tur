# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-05 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20171005_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_value',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='tour_discount',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=3),
        ),
        migrations.AddField(
            model_name='order',
            name='tour_value',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=3),
        ),
    ]