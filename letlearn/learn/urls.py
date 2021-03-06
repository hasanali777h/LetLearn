from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'learn'
urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('articles/', views.articles, name='articles'),
    path('advisorayboard/', views.advisorayboard, name='advisorayboard'),
    path('webadd/', views.webadd, name='webadd'),
    path('websitereview/', views.websitereview, name='websitereview'),
    path('helpcategory/', views.helpcategory, name='helpcategory'),
    path('subscribers/', views.subscribers, name='subscribers'),
    path('donar/', views.donar, name='donar'),
    path('businessoffertype/', views.businessoffertype, name='businessoffertype'),
    path('bank/', views.bank, name='bank'),
    path('businessoffer/', views.businessoffer, name='businessoffer'),
    path('blogtype/', views.blogtype, name='blogtype'),
    path('section/', views.section, name='section'),
    path('rolename/', views.rolename, name='rolename'),
    path('category/', views.category, name='category'),
    path('answer/', views.answer, name='answer'),
    path('articletype/', views.articletype, name='articletype'),
    path('status/', views.status, name='status'),
    path('certificatetype/', views.certificatetype, name='certificatetype'),
    path('clientmessage/', views.clientmessage, name='clientmessage'),
    path('clientreply/', views.clientreply, name='clientreply'),
    path('collabortaions/', views.collaborations, name='collaborations'),
    path('tblclass/', views.tblclass, name='tblclass'),
    path('school/', views.school, name='school'),
    path('day/', views.day, name='day'),
    path('department/', views.department, name='department'),
    path('departmentboard/', views.departmentboard, name='departmentboard'),
    path('replies/', views.replies, name='replies'),
    path('event/', views.event, name='event'),
    path('superadmin/', views.superadmin, name='superadmin'),
    path('exam/', views.exam, name='exam'),
    path('transcationtypes/', views.transcationtypes, name='transcationtypes'),
    path('quizcontext/', views.quizcontext, name='quizcontext'),
    path('student/', views.student, name='student'),
    path('course/', views.course, name='course'),
    path('teacher/', views.teacher, name='teacher'),
    path('schoolassignment/', views.schoolassignment, name='schoolassignment'),
    path('announcement/', views.announcement, name='announcement'),
    path('articlecomments/', views.articlecomments, name='articlecomments'),
    path('submitassignment/', views.submitassignment, name='submitassignment'),
    path('assignmentresult/', views.assignmentresult, name='assignmentresult'),
    path('blog/', views.blog, name='blog'),
    path('client/', views.client, name='client'),
    path('certificate/', views.certificate, name='certificate'),
    path('clientschoolcomplain/', views.clientschoolcomplain,
         name='clientschoolcomplain'),
    path('clientcertificate/', views.clientcertificate, name='clientcertificate'),
    path('comments/', views.comments, name='comments'),
    path('courseassigntoteacher/', views.courseassigntoteacher,
         name='courseassigntoteacher'),
    path('discussion/', views.discussion, name='discussion'),
    path('helps/', views.helps, name='helps'),
    path('kidsstorytype/', views.kidsstorytype, name='kidsstorytype'),
    path('kidsstory/', views.kidsstory, name='kidsstory'),
    path('kidtalent/', views.kidtalent, name='kidtalent'),
    path('lecture/', views.lecture, name='lecture'),
    path('login/', views.login, name='login'),
    path('manualtest/', views.manualtest, name='manualtest'),
    path('messages/', views.messages, name='messages'),
    path('questions/', views.questions, name='questions'),
    path('onlinetest/', views.onlinetest, name='onlinetest'),
    path('onlinetestanswers/', views.onlinetestanswers, name='onlinetestanswers'),
    path('onlinetestquestionoption/', views.onlinetestquestionoption,
         name='onlinetestquestionoption'),
    path('onlinetestresult/', views.onlinetestresult, name='onlinetestresult'),
    path('options/', views.options, name='options'),
    path('paymentconfirmation/', views.paymentconfirmation,
         name='paymentconfirmation'),
    path('post/', views.post, name='post'),
    path('quizcontextresult/', views.quizcontextresult, name='quizcontextresult'),
    path('resultclient/', views.resultclient, name='resultclient'),
    path('studentcomplain/', views.studentcomplain, name='studentcomplain'),
    path('studenthistory/', views.studenthistory, name='studenthistory'),
    path('studentmaster/', views.studentmaster, name='studentmaster'),
    path('studentresult/', views.studentresult, name='studentresult'),
    path('submitmanualtest/', views.submitmanualtest, name='submitmanualtest'),
    path('team/', views.team, name='team'),
    path('technictip/', views.technictip, name='technictip'),
    path('timetable/', views.timetable, name='timetable'),
    path('userenrollincourse/', views.userenrollincourse,
         name='userenrollincourse'),
    path('userfeedback/', views.userfeedback, name='userfeedback'),
    path('attendances/', views.attendances, name='attendances'),
    path('calender/', views.calender, name='calender'),
    path('parents/', views.parents, name='parents'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
