# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20150816_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='mycountry',
            field=models.CharField(default=b'US', max_length=2, choices=[(b'SD', b'Sudan'), (b'QR', b'Qatar'), (b'US', b'Usa')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'published on '),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, verbose_name=b'OMDERMAN'),
        ),
    ]
