# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_remove_news_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='subject',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
