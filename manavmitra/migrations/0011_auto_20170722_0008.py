# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-21 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manavmitra', '0010_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
