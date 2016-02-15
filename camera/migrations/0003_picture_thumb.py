# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0002_auto_20150604_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='thumb',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
