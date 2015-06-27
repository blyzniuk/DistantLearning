# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Subjects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='themes',
            name='theme_max_result',
        ),
        migrations.AddField(
            model_name='students',
            name='student_email',
            field=models.EmailField(max_length=70, verbose_name=b'E-mail \xd1\x81\xd1\x82\xd1\x83\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0', blank=True),
        ),
    ]
