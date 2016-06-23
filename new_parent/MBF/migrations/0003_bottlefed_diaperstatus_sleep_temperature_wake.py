# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MBF', '0002_babyevent_breastfed'),
    ]

    operations = [
        migrations.CreateModel(
            name='BottleFed',
            fields=[
                ('babyevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MBF.BabyEvent')),
                ('amount', models.PositiveSmallIntegerField()),
            ],
            bases=('MBF.babyevent',),
        ),
        migrations.CreateModel(
            name='DiaperStatus',
            fields=[
                ('babyevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MBF.BabyEvent')),
                ('diaper', models.CharField(choices=[('PO', 'Poo'), ('PE', 'Pee'), ('BO', 'Poo & Pee')], default='PE', max_length=2)),
            ],
            bases=('MBF.babyevent',),
        ),
        migrations.CreateModel(
            name='Sleep',
            fields=[
                ('babyevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MBF.BabyEvent')),
                ('sleep_status', models.CharField(choices=[('NP', 'Nap'), ('NT', 'Night')], default='NT', max_length=2)),
            ],
            bases=('MBF.babyevent',),
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('babyevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MBF.BabyEvent')),
                ('temp', models.CharField(choices=[('NO', 'Normal'), ('WM', 'Warm'), ('HO', 'Hot')], default='NO', max_length=2)),
            ],
            bases=('MBF.babyevent',),
        ),
        migrations.CreateModel(
            name='Wake',
            fields=[
                ('babyevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MBF.BabyEvent')),
                ('wake_status', models.CharField(choices=[('NP', 'Nap'), ('NT', 'Night')], default='NT', max_length=2)),
            ],
            bases=('MBF.babyevent',),
        ),
    ]