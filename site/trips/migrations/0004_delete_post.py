# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 18:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_auto_20160830_0207'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
