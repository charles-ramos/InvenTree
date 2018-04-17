# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-16 14:23
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='buildoutput',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='buildoutput',
            name='build',
        ),
        migrations.RemoveField(
            model_name='buildoutput',
            name='part',
        ),
        migrations.AddField(
            model_name='build',
            name='quantity',
            field=models.PositiveIntegerField(default=1, help_text='Number of parts to build', validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.DeleteModel(
            name='BuildOutput',
        ),
    ]
