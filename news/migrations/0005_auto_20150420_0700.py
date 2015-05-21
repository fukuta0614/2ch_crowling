# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20150420_0659'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('id', 'base_site', 'link', 'title')},
        ),
    ]
