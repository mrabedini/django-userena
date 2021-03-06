# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userena', '0002_auto_20170214_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='userenasignup',
            name='invitation_key',
            field=models.CharField(blank=True, max_length=40, verbose_name='invitation key'),
        ),
        migrations.AddField(
            model_name='userenasignup',
            name='invitation_status',
            field=models.CharField(choices=[('INV', 'Invitation Mail was sent'), ('PSWRST', 'Password was reset by user'), ('PRFEDIT', 'Profile was edited by user')], default='INV', max_length=7),
        ),
    ]
