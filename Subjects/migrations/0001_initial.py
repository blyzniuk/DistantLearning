# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_text', models.CharField(max_length=100, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd0\xb2\xd1\x96\xd0\xb4\xd0\xbf\xd0\xbe\xd0\xb2\xd1\x96\xd0\xb4\xd1\x96')),
                ('answer_price', models.IntegerField(verbose_name=b'\xd0\x9a\xd1\x96\xd0\xbb\xd1\x8c\xd0\xba\xd1\x96\xd1\x81\xd1\x82\xd1\x8c \xd0\xb1\xd0\xb0\xd0\xbb\xd1\x96\xd0\xb2 \xd0\xb7\xd0\xb0 \xd0\xb2\xd1\x96\xd0\xb4\xd0\xbf\xd0\xbe\xd0\xb2\xd1\x96\xd0\xb4\xd1\x8c')),
            ],
            options={
                'db_table': 'answers',
                'verbose_name': '\u0412\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u044c',
                'verbose_name_plural': '\u0412\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u0456',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd1\x8f')),
                ('comment_date', models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb4\xd0\xbe\xd0\xb4\xd0\xb0\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8f \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd1\x8f')),
                ('comment_rate', models.IntegerField(verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb9\xd1\x82\xd0\xb8\xd0\xbd\xd0\xb3 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd1\x8f')),
            ],
            options={
                'db_table': 'comments',
                'verbose_name': '\u041a\u043e\u043c\u0435\u043d\u0442\u0430\u0440',
                'verbose_name_plural': '\u041a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0456',
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_title', models.CharField(max_length=20, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0 \xd0\xba\xd1\x83\xd1\x80\xd1\x81\xd1\x83')),
                ('course_description', models.CharField(max_length=300, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb8\xd1\x81\xd0\xbb\xd0\xb0 \xd1\x96\xd0\xbd\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x86\xd1\x96\xd1\x8f \xd0\xbf\xd1\x80\xd0\xbe \xd0\xba\xd1\x83\xd1\x80\xd1\x81')),
                ('course_text', models.TextField(verbose_name=b'\xd0\xa0\xd0\xbe\xd0\xb7\xd0\xb3\xd0\xbe\xd1\x80\xd0\xbd\xd1\x83\xd1\x82\xd0\xb0 \xd1\x96\xd0\xbd\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x86\xd1\x96\xd1\x8f \xd0\xbf\xd1\x80\xd0\xbe \xd0\xba\xd1\x83\xd1\x80\xd1\x81')),
                ('course_img', models.ImageField(upload_to=b'media', verbose_name=b'\xd0\x86\xd0\xbb\xd1\x8e\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x86\xd1\x96\xd1\x8f \xd0\xb4\xd0\xbe \xd0\xba\xd1\x83\xd1\x80\xd1\x81\xd1\x83', blank=True)),
            ],
            options={
                'db_table': 'courses',
                'verbose_name': '\u041a\u0443\u0440\u0441',
                'verbose_name_plural': '\u041a\u0443\u0440\u0441\u0438',
            },
        ),
        migrations.CreateModel(
            name='CoursesGraduate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result', models.IntegerField(verbose_name=b'\xd0\x9e\xd1\x86\xd1\x96\xd0\xbd\xd0\xba\xd0\xb0 \xd0\xb7\xd0\xb0 \xd0\xba\xd1\x83\xd1\x80\xd1\x81')),
                ('course', models.ForeignKey(to='Subjects.Courses')),
            ],
            options={
                'db_table': 'courses_graduate',
            },
        ),
        migrations.CreateModel(
            name='CoursesStudents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.ForeignKey(to='Subjects.Courses')),
            ],
            options={
                'db_table': 'courses_students',
            },
        ),
        migrations.CreateModel(
            name='ExpandAnswersSamples',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('expand_answer_sample_text', models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd1\x80\xd0\xbe\xd0\xb7\xd0\xb3\xd0\xbe\xd1\x80\xd0\xbd\xd1\x83\xd1\x82\xd0\xbe\xd1\x97 \xd0\xb2\xd1\x96\xd0\xb4\xd0\xbf\xd0\xbe\xd0\xb2\xd1\x96\xd0\xb4\xd1\x96')),
                ('expand_answer_price', models.IntegerField(verbose_name=b'\xd0\x9c\xd0\xb0\xd0\xba\xd1\x81\xd0\xb8\xd0\xbc\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb0 \xd0\xba\xd1\x96\xd0\xbb\xd1\x8c\xd0\xba\xd1\x96\xd1\x81\xd1\x82\xd1\x8c \xd0\xb1\xd0\xb0\xd0\xbb\xd1\x96\xd0\xb2 \xd0\xb7\xd0\xb0 \xd0\xb2\xd1\x96\xd0\xb4\xd0\xbf\xd0\xbe\xd0\xb2\xd1\x96\xd0\xb4\xd1\x8c')),
            ],
            options={
                'db_table': 'expand_answers_samples',
                'verbose_name': '\u0420\u043e\u0437\u0433\u043e\u0440\u043d\u0443\u0442\u0430 \u0432\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u044c',
                'verbose_name_plural': '\u0420\u043e\u0437\u0433\u043e\u0440\u043d\u0443\u0442\u0456 \u0432\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u0456',
            },
        ),
        migrations.CreateModel(
            name='Lectures',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lecture_video', models.CharField(max_length=100, verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x81\xd0\xb8\xd0\xbb\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8f \xd0\xbd\xd0\xb0 \xd0\xb2\xd1\x96\xd0\xb4\xd0\xb5\xd0\xbe \xd0\xbd\xd0\xb0 YouTube')),
                ('lecture_plan', models.TextField(verbose_name=b'\xd0\x9f\xd0\xbb\xd0\xb0\xd0\xbd \xd0\xbb\xd0\xb5\xd0\xba\xd1\x86\xd1\x96\xd1\x97')),
                ('lecture_text', models.TextField(verbose_name=b'\xd0\x9b\xd0\xb5\xd0\xba\xd1\x86\xd1\x96\xd1\x8f')),
                ('lecture_pdf_file', models.FileField(upload_to=b'media', verbose_name=b'PDF \xd1\x84\xd0\xb0\xd0\xb9\xd0\xbb \xd0\xb7 \xd0\xbb\xd0\xb5\xd0\xba\xd1\x86\xd1\x96\xd1\x94\xd1\x8e')),
            ],
            options={
                'db_table': 'lectures',
                'verbose_name': '\u041b\u0435\u043a\u0446\u0456\u044f',
                'verbose_name_plural': '\u041b\u0435\u043a\u0446\u0456\u0457',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd0\xbf\xd0\xb8\xd1\x82\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8f')),
            ],
            options={
                'db_table': 'questions',
                'verbose_name': '\u041f\u0438\u0442\u0430\u043d\u043d\u044f',
                'verbose_name_plural': '\u041f\u0438\u0442\u0430\u043d\u043d\u044f',
            },
        ),
        migrations.CreateModel(
            name='QuestionsTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_type_title', models.CharField(max_length=20, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xbf\xd0\xb8\xd1\x82\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8f')),
            ],
            options={
                'db_table': 'questions_types',
                'verbose_name': '\u0422\u0438\u043f \u043f\u0438\u0442\u0430\u043d\u043d\u044f',
                'verbose_name_plural': '\u0422\u0438\u043f\u0438 \u043f\u0438\u0442\u0430\u043d\u043d\u044c',
            },
        ),
        migrations.CreateModel(
            name='StandbyResults',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('standby_results_previous_result', models.IntegerField(verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb7\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x82 \xd0\xb7\xd0\xb0 \xd1\x82\xd0\xb5\xd1\x81\xd1\x82\xd0\xb8')),
                ('standby_results_verified_expands', models.BooleanField(default=False, verbose_name=b'\xd0\xa7\xd0\xb8 \xd0\xbf\xd0\xb5\xd1\x80\xd0\xb5\xd0\xb2\xd1\x96\xd1\x80\xd0\xb8\xd0\xb2 \xd0\xb0\xd0\xb4\xd0\xbc\xd1\x96\xd0\xbd\xd1\x96\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80 \xd1\x80\xd0\xbe\xd0\xb7\xd0\xb3\xd0\xbe\xd1\x80\xd0\xbd\xd1\x83\xd1\x82\xd1\x96 \xd0\xb2\xd1\x96\xd0\xb4\xd0\xbf\xd0\xbe\xd0\xb2\xd1\x96\xd0\xb4\xd1\x96')),
            ],
            options={
                'db_table': 'standby_results',
                'verbose_name': '\u0412 \u043e\u0447\u0456\u043a\u0443\u0432\u0430\u043d\u043d\u0456 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0443',
                'verbose_name_plural': '\u0412 \u043e\u0447\u0456\u043a\u0443\u0432\u0430\u043d\u043d\u0456 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0443',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_courses_active', models.ManyToManyField(related_name='courses_active', through='Subjects.CoursesStudents', to='Subjects.Courses')),
                ('student_courses_finished', models.ManyToManyField(related_name='courses_finished', through='Subjects.CoursesGraduate', to='Subjects.Courses')),
            ],
            options={
                'db_table': 'students',
                'verbose_name': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442',
                'verbose_name_plural': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u0438',
            },
        ),
        migrations.CreateModel(
            name='StudentsExpandAnswers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('students_expand_answer_text', models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd1\x80\xd0\xbe\xd0\xb7\xd0\xb3\xd0\xbe\xd1\x80\xd0\xbd\xd1\x83\xd1\x82\xd0\xbe\xd1\x97 \xd0\xb2\xd1\x96\xd0\xb4\xd0\xbf\xd0\xbe\xd0\xb2\xd1\x96\xd0\xb4\xd1\x96 \xd1\x81\xd1\x82\xd1\x83\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0')),
                ('students_expand_answer_author', models.ForeignKey(to='Subjects.Students')),
                ('students_expand_answer_question', models.ForeignKey(to='Subjects.Questions')),
            ],
            options={
                'db_table': 'students_expand_answers',
                'verbose_name': '\u0420\u043e\u0437\u0433\u043e\u0440\u043d\u0443\u0442\u0430 \u0432\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u044c \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430',
                'verbose_name_plural': '\u0420\u043e\u0437\u0433\u043e\u0440\u043d\u0443\u0442\u0456 \u0432\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u0456 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0456\u0432',
            },
        ),
        migrations.CreateModel(
            name='StudentsVotedComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.ForeignKey(to='Subjects.Comments')),
                ('student', models.ForeignKey(to='Subjects.Students')),
            ],
            options={
                'db_table': 'students_voted_comments',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_title', models.CharField(max_length=15, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0 \xd0\xbd\xd0\xb0\xd0\xbf\xd1\x80\xd1\x8f\xd0\xbc\xd1\x83')),
            ],
            options={
                'db_table': 'subjects',
                'verbose_name': '\u041d\u0430\u043f\u0440\u044f\u043c',
                'verbose_name_plural': '\u041d\u0430\u043f\u0440\u044f\u043c\u0438',
            },
        ),
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('theme_title', models.CharField(max_length=30, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0 \xd1\x82\xd0\xb5\xd0\xbc\xd0\xb8')),
                ('theme_max_result', models.IntegerField(verbose_name=b'\xd0\x9c\xd0\xb0\xd0\xba\xd1\x81\xd0\xb8\xd0\xbc\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb8\xd0\xb9 \xd0\xbc\xd0\xbe\xd0\xb6\xd0\xbb\xd0\xb8\xd0\xb2\xd0\xb8\xd0\xb9 \xd0\xb1\xd0\xb0\xd0\xbb')),
                ('theme_course', models.ForeignKey(to='Subjects.Courses')),
            ],
            options={
                'db_table': 'themes',
                'verbose_name': '\u0422\u0435\u043c\u0430',
                'verbose_name_plural': '\u0422\u0435\u043c\u0438',
            },
        ),
        migrations.CreateModel(
            name='ThemesGraduate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result', models.IntegerField(verbose_name=b'\xd0\x9e\xd1\x86\xd1\x96\xd0\xbd\xd0\xba\xd0\xb0 \xd0\xb7\xd0\xb0 \xd1\x82\xd0\xb5\xd0\xbc\xd1\x83')),
                ('student', models.ForeignKey(to='Subjects.Students')),
                ('theme', models.ForeignKey(to='Subjects.Themes')),
            ],
            options={
                'db_table': 'themes_graduate',
            },
        ),
        migrations.AddField(
            model_name='themes',
            name='theme_graduate',
            field=models.ManyToManyField(to='Subjects.Students', verbose_name=b'\xd0\xa2\xd1\x96 \xd1\x85\xd1\x82\xd0\xbe \xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbb\xd0\xb8 \xd1\x82\xd0\xb5\xd0\xbc\xd1\x83', through='Subjects.ThemesGraduate'),
        ),
        migrations.AddField(
            model_name='students',
            name='student_themes_passed',
            field=models.ManyToManyField(to='Subjects.Themes', through='Subjects.ThemesGraduate'),
        ),
        migrations.AddField(
            model_name='students',
            name='student_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='students',
            name='student_voted_comments',
            field=models.ManyToManyField(to='Subjects.Comments', through='Subjects.StudentsVotedComments'),
        ),
        migrations.AddField(
            model_name='standbyresults',
            name='standby_results_student',
            field=models.ForeignKey(to='Subjects.Students'),
        ),
        migrations.AddField(
            model_name='standbyresults',
            name='standby_results_theme',
            field=models.ForeignKey(to='Subjects.Themes'),
        ),
        migrations.AddField(
            model_name='questions',
            name='question_theme',
            field=models.ForeignKey(to='Subjects.Themes'),
        ),
        migrations.AddField(
            model_name='questions',
            name='question_type',
            field=models.ForeignKey(to='Subjects.QuestionsTypes'),
        ),
        migrations.AddField(
            model_name='lectures',
            name='lecture_theme',
            field=models.ForeignKey(to='Subjects.Themes'),
        ),
        migrations.AddField(
            model_name='expandanswerssamples',
            name='expand_answer_sample_question',
            field=models.ForeignKey(to='Subjects.Questions'),
        ),
        migrations.AddField(
            model_name='coursesstudents',
            name='student',
            field=models.ForeignKey(to='Subjects.Students'),
        ),
        migrations.AddField(
            model_name='coursesgraduate',
            name='student',
            field=models.ForeignKey(to='Subjects.Students'),
        ),
        migrations.AddField(
            model_name='courses',
            name='course_graduate',
            field=models.ManyToManyField(related_name='course_graduate', verbose_name=b'\xd0\x92\xd0\xb8\xd0\xbf\xd1\x83\xd1\x81\xd0\xba\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb8 \xd0\xba\xd1\x83\xd1\x80\xd1\x81\xd1\x83', through='Subjects.CoursesGraduate', to='Subjects.Students'),
        ),
        migrations.AddField(
            model_name='courses',
            name='course_student',
            field=models.ManyToManyField(related_name='course_student', verbose_name=b'\xd0\xa1\xd0\xbb\xd1\x83\xd1\x85\xd0\xb0\xd1\x87\xd1\x96 \xd0\xba\xd1\x83\xd1\x80\xd1\x81\xd1\x83', through='Subjects.CoursesStudents', to='Subjects.Students'),
        ),
        migrations.AddField(
            model_name='courses',
            name='course_subject',
            field=models.ForeignKey(to='Subjects.Subject'),
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_author',
            field=models.ForeignKey(related_name='comment_author', to='Subjects.Students'),
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_course',
            field=models.ForeignKey(to='Subjects.Courses'),
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_voted_users',
            field=models.ManyToManyField(related_name='voted_users', through='Subjects.StudentsVotedComments', to='Subjects.Students'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer_question',
            field=models.ForeignKey(to='Subjects.Questions'),
        ),
    ]
