# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20150423_0239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='creator',
        ),
    ]
