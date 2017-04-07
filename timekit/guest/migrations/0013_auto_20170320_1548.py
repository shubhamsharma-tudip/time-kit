# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 15:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0012_calender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calender',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]