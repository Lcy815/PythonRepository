# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-16 05:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_views'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-create_time']},
        ),
    ]
