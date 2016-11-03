# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-19 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djadmin', '0007_auto_20161015_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuinfo',
            name='menu_link',
            field=models.CharField(max_length=255, null=True, verbose_name='\u94fe\u63a5'),
        ),
        migrations.AddField(
            model_name='menuinfo',
            name='menu_pid',
            field=models.IntegerField(null=True, verbose_name='\u4e0a\u7ea7\u83dc\u5355'),
        ),
        migrations.AddField(
            model_name='menuinfo',
            name='menu_visible',
            field=models.IntegerField(default=1, null=True, verbose_name='\u662f\u5426\u53ef\u89c1'),
        ),
        migrations.AlterField(
            model_name='menuinfo',
            name='menu_order',
            field=models.IntegerField(null=True, verbose_name='\u6392\u5e8f'),
        ),
    ]