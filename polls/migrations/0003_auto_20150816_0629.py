# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_your_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='mycountry',
            field=models.CharField(default=b'SD', max_length=20, choices=[(b'SD', b'Sd'), (b'QR', b'Qr'), (b'US', b'Us')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='your_name',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
