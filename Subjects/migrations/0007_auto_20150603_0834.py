# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Subjects', '0006_auto_20150603_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='answer_price',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\x9a\xd1\x96\xd0\xbb\xd1\x8c\xd0\xba\xd1\x96\xd1\x81\xd1\x82\xd1\x8c \xd0\xb1\xd0\xb0\xd0\xbb\xd1\x96\xd0\xb2 \xd0\xb7\xd0\xb0 \xd0\xb2\xd1\x96\xd0\xb4\xd0\xbf\xd0\xbe\xd0\xb2\xd1\x96\xd0\xb4\xd1\x8c'),
        ),
    ]
