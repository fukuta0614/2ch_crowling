# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20150421_0208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='description',
        ),
        migrations.RemoveField(
            model_name='news',
            name='encoded',
        ),
    ]
