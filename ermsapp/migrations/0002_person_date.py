# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ermsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='Date',
            field=models.DateField(default=datetime.datetime(2016, 6, 23, 18, 27, 2, 165444, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
