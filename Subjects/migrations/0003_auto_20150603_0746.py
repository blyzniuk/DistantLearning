# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Subjects', '0002_auto_20150602_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expandanswerssamples',
            name='expand_answer_sample_question',
        ),
        migrations.DeleteModel(
            name='ExpandAnswersSamples',
        ),
    ]
