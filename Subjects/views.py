# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from models import *
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from forms import CommentForm
import datetime
# Create your views here.

def courses(request, subject_id):
    args = {}
    args['subject_title'] = Subject.objects.get(id=subject_id).subject_title
    args['subjects'] = Subject.objects.all()
    args['courses'] = Courses.objects.filter(course_subject_id=subject_id)
    args['user'] = auth.get_user(request)
    return render_to_response('courses.html', args)

def all_courses(request):
    args = {}
    args['subjects'] = Subject.objects.all()
    args['courses'] = Courses.objects.all()
    args['user'] = auth.get_user(request)
    return render_to_response('allcourses.html', args)

def course(request, course_id):
    args = {}
    args['subjects'] = Subject.objects.all()
    args['course'] = Courses.objects.get(id=course_id)
    args['themes'] = Themes.objects.filter(theme_course_id=course_id)
    args['comments'] = Comments.objects.filter(comment_course_id=course_id).order_by('-comment_rate')[0:3]
    args['user'] = auth.get_user(request)
    try:
        Students.objects.get(student_user_id=args['user'].id)
        args['user_is_student'] = True
    except ObjectDoesNotExist:
        args['user_is_student'] = False
    return render_to_response('course.html', args)

def lecture(request, theme_id):
    args = {}
    args['subjects'] = Subject.objects.all()
    args['theme_title'] = Themes.objects.get(id=theme_id).theme_title
    args['lecture'] = Lectures.objects.get(lecture_theme_id=theme_id)
    args['user'] = auth.get_user(request)
    return render_to_response('lecture.html', args)

def test(request, theme_id):
    args = {}
    args['subjects'] = Subject.objects.all()
    args['theme_title'] = Themes.objects.get(id=theme_id).theme_title
    args['questions'] = Questions.objects.filter(question_theme_id=theme_id)
    args['answers'] = []
    for question in args['questions']:
        args['answers'].append(Answers.objects.filter(answer_question_id=question.id))
    args['user'] = auth.get_user(request)
    return render_to_response('test.html', args)

def feedback(request, course_id):
    args = {}
    args.update(csrf(request))
    args['subjects'] = Subject.objects.all()
    args['course_title'] = Courses.objects.get(id=course_id).course_title
    args['course_id'] = course_id
    args['comments'] = Comments.objects.filter(comment_course_id=course_id)
    args['user'] = auth.get_user(request)
    return render_to_response('feedback.html', args)

def profile(request, user_id):
    student = Students.objects.get(student_user_id=user_id)
    args = {}
    args['subjects'] = Subject.objects.all()
    args['finished_courses'] = CoursesGraduate.objects.filter(student=student)
    args['active_courses'] = CoursesStudents.objects.filter(student=student)
    args['themes_passed'] = student.student_themes_passed
    args['user'] = auth.get_user(request)
    return render_to_response('profile.html', args)

def start_page(request):
    args = {}
    args['subjects'] = Subject.objects.all()
    for subject in args['subjects']:
        args['course_%s' %subject.id] = Courses.objects.filter(course_subject_id=subject.id)
    args['user'] = auth.get_user(request)
    return render_to_response('startpage.html',args)

def login(request):
    args = {}
    args['subjects'] = Subject.objects.all()
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                auth.login(request, user)
                return redirect('/admin/')

            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'Користувача не знайдено'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    args = {}
    args['subjects'] = Subject.objects.all()
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            newuser = auth.authenticate(username=new_user_form.cleaned_data['username'],password=new_user_form.cleaned_data['password2'])
            auth.login(request,newuser)
            user = Students(student_user_id=newuser.id,student_email='testmail@mail.com')
            user.save()
            return redirect('/')
        else:
            args['form'] = new_user_form
    return render_to_response('register.html', args)

def register2(request):
    args = {}
    args['subjects'] = Subject.objects.all()
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password1 = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '')
        if (username):
            auth.login(request, user)

            return redirect('/')
        else:
            args['login_error'] = 'Користувача не знайдено'
            return render_to_response('register.html', args)
    else:
        return render_to_response('register.html', args)

def addcomment(request, course_id):
    args = {}
    args.update(csrf(request))
    args['subjects'] = Subject.objects.all()
    args['course_title'] = Courses.objects.get(id=course_id).course_title
    args['course_id'] = course_id
    args['comments'] = Comments.objects.filter(comment_course_id=course_id)
    args['user'] = auth.get_user(request)
    if auth.get_user(request).get_username():
        if request.POST:
            comment_text = request.POST.get('comment_text', '')
            if comment_text:
                comment = Comments()
                comment.comment_text = comment_text
                comment.comment_rate = 0
                comment.comment_course_id = course_id
                comment.comment_author_id =  Students.objects.get(student_user_id=auth.get_user(request).id).id
                comment.comment_date = datetime.datetime.now()
                comment.save()
                return redirect('/feedback/%s/' % course_id)
            else:
                args['comment_error'] = 'Введіть коментар'
                return render_to_response('feedback.html', args)
    else:
        args['comment_error'] = "Коментарі можуть лишати лише авторизовані користувачі"
    return render_to_response('feedback.html', args)

def like(request, comment_id):
    comment = Comments.objects.get(id=comment_id)
    user = auth.get_user(request)
    if not user.get_username():
        return redirect('/feedback/%s/' %comment.comment_course.id)
    student = Students.objects.get(student_user_id=user.id)
    if comment.comment_voted_users.filter(id=student.id):
        return redirect('/feedback/%s/' %comment.comment_course.id)
    comment.comment_rate += 1
    comment.save()
    vote = StudentsVotedComments(comment=comment,student=student)
    vote.save()
    return redirect('/feedback/%s/' %comment.comment_course.id)

def dislike(request, comment_id):
    comment = Comments.objects.get(id=comment_id)
    user = auth.get_user(request)
    if not user.get_username():
        return redirect('/feedback/%s/' %comment.comment_course.id)
    student = Students.objects.get(student_user_id=user.id)
    if comment.comment_voted_users.filter(id=student.id):
        return redirect('/feedback/%s/' %comment.comment_course.id)
    comment.comment_rate -= 1
    comment.save()
    vote = StudentsVotedComments(comment=comment,student=student)
    vote.save()
    return redirect('/feedback/%s/' %comment.comment_course.id)