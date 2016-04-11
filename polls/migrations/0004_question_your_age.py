# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20150816_0629'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='your_age',
            field=models.CharField(default=b'mohamed wdalnor', max_length=200),
        ),
    ]
