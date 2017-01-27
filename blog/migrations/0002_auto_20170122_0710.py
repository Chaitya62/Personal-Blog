# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-22 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published!', 'Published')], default='draft', max_length=10),
        ),
    ]
