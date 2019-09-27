# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-15 07:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField()),
                ('hcomment', models.CharField(max_length=100)),
                ('hbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest.BookInfo')),
            ],
        ),
    ]
