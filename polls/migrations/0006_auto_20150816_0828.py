# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20150816_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='mycountry',
            field=models.CharField(default=b'SD', max_length=2, choices=[(b'sudan', b'Sd'), (b'qatar', b'Qr'), (b'usa', b'Us')]),
        ),
    ]
