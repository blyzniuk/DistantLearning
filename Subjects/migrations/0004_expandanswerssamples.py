# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Subjects', '0003_auto_20150603_0746'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpandAnswersSamples',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('expand_answer_sample_text', models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd1\x80\xd0\xbe\xd0\xb7\xd0\xb3\xd0\xbe\xd1\x80\xd0\xbd\xd1\x83\xd1\x82\xd0\xbe\xd1\x97 \xd0\xb2\xd1\x96\xd0\xb4\xd0\xbf\xd0\xbe\xd0\xb2\xd1\x96\xd0\xb4\xd1\x96')),
                ('expand_answer_price', models.IntegerField(verbose_name=b'\xd0\x9c\xd0\xb0\xd0\xba\xd1\x81\xd0\xb8\xd0\xbc\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb0 \xd0\xba\xd1\x96\xd0\xbb\xd1\x8c\xd0\xba\xd1\x96\xd1\x81\xd1\x82\xd1\x8c \xd0\xb1\xd0\xb0\xd0\xbb\xd1\x96\xd0\xb2 \xd0\xb7\xd0\xb0 \xd0\xb2\xd1\x96\xd0\xb4\xd0\xbf\xd0\xbe\xd0\xb2\xd1\x96\xd0\xb4\xd1\x8c')),
                ('expand_answer_sample_question', models.ForeignKey(to='Subjects.Questions')),
            ],
            options={
                'db_table': 'expand_answers_samples',
                'verbose_name': '\u0420\u043e\u0437\u0433\u043e\u0440\u043d\u0443\u0442\u0430 \u0432\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u044c',
                'verbose_name_plural': '\u0420\u043e\u0437\u0433\u043e\u0440\u043d\u0443\u0442\u0456 \u0432\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u0456',
            },
        ),
    ]
