# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='personInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Age', models.IntegerField()),
                ('Address', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=10)),
            ],
        ),
    ]
