# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-20 00:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djadmin', '0008_auto_20161019_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='menu_type',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
    ]
