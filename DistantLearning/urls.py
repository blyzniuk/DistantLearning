"""DistantLearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^courses/(?P<subject_id>\d+)/$', 'Subjects.views.courses'),
    url(r'^courses/$', 'Subjects.views.all_courses'),
    url(r'^course/(?P<course_id>\d+)/$', 'Subjects.views.course'),
    url(r'^lecture/(?P<theme_id>\d+)/$', 'Subjects.views.lecture'),
    url(r'^test/(?P<theme_id>\d+)/$', 'Subjects.views.test'),
    url(r'^feedback/(?P<course_id>\d+)/addcomment/$', 'Subjects.views.addcomment'),
    url(r'^feedback/(?P<course_id>\d+)/$', 'Subjects.views.feedback'),
    url(r'^comment/(?P<comment_id>\d+)/dislike/$', 'Subjects.views.dislike'),
    url(r'^comment/(?P<comment_id>\d+)/like/$', 'Subjects.views.like'),
    url(r'^feedback/(?P<course_id>\d+)/$', 'Subjects.views.feedback'),
    url(r'^profile/(?P<user_id>\d+)/$', 'Subjects.views.profile'),
    url(r'^login/', 'Subjects.views.login'),
    url(r'^logout/', 'Subjects.views.logout'),
    url(r'^register/', 'Subjects.views.register'),
    url(r'^$', 'Subjects.views.start_page'),
]
