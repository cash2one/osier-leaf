# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-15 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djadmin', '0004_auto_20161015_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=30, verbose_name='\u83dc\u5355\u540d\u79f0')),
                ('menu_link', models.CharField(max_length=30, verbose_name='\u83dc\u5355\u94fe\u63a5')),
                ('menu_pid', models.IntegerField(null=True, verbose_name='\u4e0a\u7ea7\u83dc\u5355')),
                ('menu_order', models.IntegerField(null=True, verbose_name='\u83dc\u5355\u6392\u5e8f')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'db_table': 'django_menu_info',
                'verbose_name': '\u7f51\u7ad9\u4fe1\u606f\u7ba1\u7406',
                'verbose_name_plural': '\u7f51\u7ad9\u4fe1\u606f\u7ba1\u7406',
            },
        ),
    ]
