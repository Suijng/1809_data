# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-28 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('zhanghao', models.CharField(max_length=50)),
                ('mima', models.CharField(max_length=50)),
                ('gender', models.IntegerField(default=0)),
            ],
        ),
    ]
