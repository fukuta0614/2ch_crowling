# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='base_site',
            field=models.CharField(default='unknown', max_length=120),
        ),
        migrations.AlterField(
            model_name='news',
            name='link',
            field=models.CharField(default='nolink', max_length=120),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(default='notitle', max_length=120),
        ),
    ]
