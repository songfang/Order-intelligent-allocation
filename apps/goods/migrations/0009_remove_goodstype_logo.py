# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-03-19 04:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_auto_20190319_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodstype',
            name='logo',
        ),
    ]