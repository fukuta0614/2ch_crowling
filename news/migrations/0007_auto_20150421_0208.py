# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20150420_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='content',
        ),
        migrations.AddField(
            model_name='news',
            name='encoded',
            field=models.TextField(null=True, blank=True),
        ),
    ]
