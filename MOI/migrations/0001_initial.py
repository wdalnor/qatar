# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emp_name', models.CharField(max_length=200)),
                ('devision', models.CharField(max_length=200)),
                ('emp_phon', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ten_num', models.CharField(max_length=100, verbose_name=b'Tender_nuumber')),
                ('date_received', models.DateTimeField(verbose_name=b'Received on')),
                ('band_num', models.IntegerField()),
                ('purch_order_number', models.IntegerField()),
                ('contract_num', models.CharField(max_length=200, verbose_name=b'contract_number')),
                ('date_closed', models.DateTimeField(verbose_name=b'closing date')),
                ('employee', models.ForeignKey(to='MOI.Employee')),
            ],
        ),
    ]
