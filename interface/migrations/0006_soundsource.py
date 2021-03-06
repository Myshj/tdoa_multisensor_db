# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 08:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0005_auto_20170118_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoundSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval', models.FloatField(default=10)),
                ('state', models.CharField(choices=[('working', 'working'), ('waiting', 'waiting'), ('broken', 'broken')], default='working', max_length=10)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.Position')),
            ],
        ),
    ]
