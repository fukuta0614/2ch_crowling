# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20150420_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
