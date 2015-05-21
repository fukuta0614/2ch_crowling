# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('link', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=120, blank=True)),
                ('creater', models.CharField(max_length=120, blank=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('subject', models.CharField(max_length=120, blank=True)),
                ('content', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('user_name', models.CharField(max_length=120, null=True, blank=True)),
            ],
        ),
    ]
