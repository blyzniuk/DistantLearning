# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Subject(models.Model):
    class Meta():
        db_table = "subjects"
        verbose_name = "Напрям"
        verbose_name_plural = "Напрями"
    def __unicode__(self):
        return self.subject_title
    subject_title = models.CharField(max_length=15, verbose_name='Назва напряму')

class Courses(models.Model):
    class Meta():
        db_table = "courses"
        verbose_name = "Курс"
        verbose_name_plural = "Курси"
    def __unicode__(self):
        return self.course_title
    course_title = models.CharField(max_length=20, verbose_name='Назва курсу')
    course_subject = models.ForeignKey(Subject)
    course_description = models.CharField(max_length=300, verbose_name='Стисла інформація про курс')
    course_text = models.TextField(verbose_name='Розгорнута інформація про курс')
    course_img = models.ImageField(upload_to='media', blank=True, verbose_name='Ілюстрація до курсу')
    #course_student = models.ManyToManyField('Students', through='CoursesStudents', verbose_name='Слухачі курсу', related_name='course_student')
    course_graduate = models.ManyToManyField('Students', through='CoursesGraduate', verbose_name='Випускники курсу', related_name='course_graduate')


class Themes(models.Model):
    class Meta():
        db_table = "themes"
        verbose_name = "Тема"
        verbose_name_plural = "Теми"
    def __unicode__(self):
        return self.theme_title
    theme_title = models.CharField(max_length=30, verbose_name='Назва теми')
    theme_course = models.ForeignKey(Courses)
    theme_graduate = models.ManyToManyField('Students', through='ThemesGraduate', verbose_name='Ті хто здали тему')

class Lectures(models.Model):
    class Meta():
        db_table = "lectures"
        verbose_name = "Лекція"
        verbose_name_plural = "Лекції"
    def __unicode__(self):
        return self.lecture_theme.theme_title
    lecture_theme = models.ForeignKey(Themes)
    lecture_video = models.CharField(max_length=100, verbose_name='Посилання на відео на YouTube')
    lecture_plan = models.TextField(verbose_name='План лекції')
    lecture_text = models.TextField(verbose_name='Лекція')
    lecture_pdf_file = models.FileField(upload_to='media', verbose_name='PDF файл з лекцією')

class Students(models.Model):
    class Meta():
        db_table = "students"
        verbose_name = "Студент"
        verbose_name_plural = "Студенти"
    def __unicode__(self):
        return User.objects.get(id=self.student_user_id).username
    student_user = models.ForeignKey(User)
    student_email = models.EmailField(max_length=70, blank=True, verbose_name='E-mail студента')
    student_themes_passed = models.ManyToManyField('Themes', through='ThemesGraduate')
    student_courses_active = models.ManyToManyField('Courses', through='CoursesStudents', related_name='courses_active')
    student_courses_finished = models.ManyToManyField('Courses', through='CoursesGraduate', related_name='courses_finished')
    student_voted_comments = models.ManyToManyField('Comments', through='StudentsVotedComments')

class Comments(models.Model):
    class Meta():
        db_table = "comments"
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"
    comment_course = models.ForeignKey(Courses)
    comment_author = models.ForeignKey(Students, related_name='comment_author')
    comment_text = models.TextField(verbose_name='Текст коментаря')
    comment_date = models.DateTimeField(verbose_name='Дата додавання коментаря')
    comment_rate = models.IntegerField(verbose_name='Рейтинг коментаря')
    comment_voted_users = models.ManyToManyField('Students', through='StudentsVotedComments', related_name='voted_users')

class ThemesGraduate(models.Model):
    class Meta():
        db_table = "themes_graduate"
    student = models.ForeignKey(Students)
    theme = models.ForeignKey(Themes)
    result = models.IntegerField(verbose_name='Оцінка за тему')

class CoursesStudents(models.Model):
    class Meta():
        db_table = "courses_students"
    student = models.ForeignKey(Students)
    course = models.ForeignKey(Courses)

class CoursesGraduate(models.Model):
    class Meta():
        db_table = "courses_graduate"
    student = models.ForeignKey(Students)
    course = models.ForeignKey(Courses)
    result = models.IntegerField(verbose_name='Оцінка за курс')

class StudentsVotedComments(models.Model):
    class Meta():
        db_table = "students_voted_comments"
    student = models.ForeignKey(Students)
    comment = models.ForeignKey(Comments)

class Questions(models.Model):
    class Meta():
        db_table = "questions"
        verbose_name = "Питання"
        verbose_name_plural = "Питання"
    def __unicode__(self):
        return self.question_text
    question_text = models.CharField(max_length=200, verbose_name='Текст питання')
    question_theme = models.ForeignKey(Themes)

class Answers(models.Model):
    class Meta():
        db_table = "answers"
        verbose_name = "Відповідь"
        verbose_name_plural = "Відповіді"
    def __unicode__(self):
        return self.answer_text
    answer_text = models.CharField(max_length=100, verbose_name='Текст відповіді')
    answer_question = models.ForeignKey(Questions)
    answer_price = models.IntegerField(default=0, verbose_name='Кількість балів за відповідь')

class StudentsExpandAnswers(models.Model):
    class Meta():
        db_table = "students_expand_answers"
        verbose_name = "Розгорнута відповідь студента"
        verbose_name_plural = "Розгорнуті відповіді студентів"
    def __unicode__(self):
        return self.students_expand_answer_text
    students_expand_answer_text = models.TextField('Текст розгорнутої відповіді студента')
    students_expand_answer_question = models.ForeignKey(Questions)
    students_expand_answer_author = models.ForeignKey(Students)

class StandbyResults(models.Model):
    class Meta():
        db_table = "standby_results"
        verbose_name = "В очікуванні результату"
        verbose_name_plural = "В очікуванні результату"
    def __unicode__(self):
        return self.standby_results_student
    standby_results_theme = models.ForeignKey(Themes)
    standby_results_student = models.ForeignKey(Students)
    standby_results_previous_result = models.IntegerField(verbose_name='Результат за тести')
    standby_results_verified_expands = models.BooleanField(default=False, verbose_name='Чи перевірив адміністратор розгорнуті відповіді')