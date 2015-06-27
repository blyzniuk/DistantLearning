# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Subjects', '0007_auto_20150603_0834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='course_student',
        ),
    ]
