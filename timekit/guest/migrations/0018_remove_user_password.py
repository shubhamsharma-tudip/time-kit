# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-28 15:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0017_user_signup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]