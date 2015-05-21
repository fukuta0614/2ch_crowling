# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20150423_0251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('date', 'id', 'base_site', 'link', 'title')},
        ),
    ]
