# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MBF', '0006_caretaker_family'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='temp',
            field=models.CharField(choices=[('normal', 'Normal'), ('warm', 'Warm'), ('hot', 'Hot')], default='normal', max_length=6),
        ),
    ]
