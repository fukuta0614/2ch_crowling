# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20150420_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
