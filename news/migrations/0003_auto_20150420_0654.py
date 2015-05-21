# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150420_0630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='creater',
            new_name='creator',
        ),
    ]
