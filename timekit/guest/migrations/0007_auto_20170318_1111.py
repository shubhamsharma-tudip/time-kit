# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0006_remove_user_api_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('timezone', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('password', models.CharField(max_length=20)),
                ('api_token', models.CharField(default=None, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
