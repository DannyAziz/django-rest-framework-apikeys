# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-25 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django-rest-framework-apikeys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apikey',
            name='key',
            field=models.CharField(blank=True, max_length=40, null=True, unique=True),
        ),
    ]
