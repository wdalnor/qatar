# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='your_name',
            field=models.CharField(default=datetime.datetime(2015, 8, 7, 7, 52, 23, 101416, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
