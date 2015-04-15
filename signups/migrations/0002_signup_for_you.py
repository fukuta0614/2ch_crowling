# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='for_you',
            field=models.BooleanField(default=True, verbose_name='Check this'),
            preserve_default=True,
        ),
    ]
