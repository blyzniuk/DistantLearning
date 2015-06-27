# -*- coding:utf-8 -*-
from django.contrib import admin
from Subjects.models import *
# Register your models here.

class QuestionInLine(admin.StackedInline):
    model = Answers
    extra = 0
class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text', 'question_theme']
    inlines = [QuestionInLine]
    list_filter = ['question_theme']


admin.site.register(Subject)
admin.site.register(Courses)
admin.site.register(Comments)
admin.site.register(Themes)
admin.site.register(Lectures)
admin.site.register(Questions, QuestionAdmin)
admin.site.register(Answers)
admin.site.register(Students)
admin.site.register(StudentsExpandAnswers)
admin.site.register(StandbyResults)

