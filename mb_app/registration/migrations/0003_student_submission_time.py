# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20160314_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='submission_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 15, 0, 47, 56, 794594, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
