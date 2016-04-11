# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_question_your_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='mycountry',
            field=models.CharField(default=b'SD', max_length=20, choices=[(b'sudan', b'Sd'), (b'qatar', b'Qr'), (b'usa', b'Us')]),
        ),
    ]
