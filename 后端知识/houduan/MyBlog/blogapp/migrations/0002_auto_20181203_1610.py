# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-03 08:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.Tags'),
        ),
    ]
