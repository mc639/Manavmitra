# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-23 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hindi', '0005_auto_20170722_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='embed',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
