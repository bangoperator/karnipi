# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='height',
            field=models.CharField(default=480, max_length=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picture',
            name='width',
            field=models.CharField(default=640, max_length=4),
            preserve_default=True,
        ),
    ]
