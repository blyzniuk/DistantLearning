# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Subjects', '0005_auto_20150603_0812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='question_type',
        ),
        migrations.DeleteModel(
            name='QuestionsTypes',
        ),
    ]
