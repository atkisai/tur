# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-05 09:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_auto_20171005_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=24, null=True)),
                ('discount', models.DecimalField(decimal_places=2, default=1, max_digits=3)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Период',
                'verbose_name_plural': 'Периоды',
            },
        ),
        migrations.AddField(
            model_name='tour',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=3),
        ),
        migrations.AddField(
            model_name='location',
            name='period',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tours.Period'),
        ),
    ]
