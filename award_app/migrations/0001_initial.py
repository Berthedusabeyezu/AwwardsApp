# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-01 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=50)),
            ],
        ),
    ]
