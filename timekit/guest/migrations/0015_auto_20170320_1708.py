# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 17:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0014_auto_20170320_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calender',
            old_name='user_name',
            new_name='user',
        ),
    ]
