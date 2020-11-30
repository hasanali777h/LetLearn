# Generated by Django 2.2.17 on 2020-11-21 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvisorayBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardid', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('departmentid', models.IntegerField()),
                ('shortdescription', models.TextField(max_length=500)),
                ('longdescription', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('parentsid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='AdvisoryBoard',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='id',
        ),
        migrations.AddField(
            model_name='attendance',
            name='attendance',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='subscribers',
            name='subname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='announcementbody',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='announcementtitle',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answertext',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='imgpath',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='longdes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='shortdes',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='articlecomments',
            name='commentdescription',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='articletype',
            name='articletypename',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attendanceid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bank',
            name='bankname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='blog',
            name='imgpath',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='longdes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='shortdes',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='blogtype',
            name='blogtypename',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='businessoffer',
            name='imgpath',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='businessoffer',
            name='longdes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='businessoffer',
            name='shortdes',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='businessoffer',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='businessoffertype',
            name='articletypename',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='categoryname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='cerificatetype',
            name='certificatetypename',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='client',
            name='certificatetypename',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='client',
            name='cnic',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='client',
            name='contactnumber',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='client',
            name='username',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='clientcertificate',
            name='percentage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='clientcertificate',
            name='username',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='clientmessage',
            name='form',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='clientmessage',
            name='messagetopost',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='clientmessage',
            name='subject',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='clientreply',
            name='replyform',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='clientreply',
            name='replymessage',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='clientschoolcomplain',
            name='complaindescription',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='clientschoolcomplain',
            name='replymsg',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='collaborations',
            name='collaborationname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='collaborations',
            name='collaborationtitle',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='collaborations',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='assignto',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='coursedescription',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='coursename',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='coursetype',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='imagelink',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='course',
            name='longdes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='videolink',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='day',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='department',
            name='departmentname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='departmentboard',
            name='departmentname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='threadtitle',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='donar',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='donar',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='donar',
            name='fathername',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='donar',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='donar',
            name='nic',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventdescription',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventvenue',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventvenuevideo',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='exam',
            name='examname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='help',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='help',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='help',
            name='fathername',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='help',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='help',
            name='nic',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='helpcategory',
            name='categoryname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='kidsstory',
            name='imgpath',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='kidsstory',
            name='longdes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='kidsstory',
            name='shortdes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='kidsstory',
            name='storytitle',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='kidsstorytype',
            name='kidsstoryname',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='kidtalent',
            name='longdes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='kidtalent',
            name='shortdes',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='kidtalent',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='kidtalent',
            name='videopath',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lecturedescription',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lecturename',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lectureurl',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='videolink',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='login',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='manualtest',
            name='testurl',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='messages',
            name='form',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='messages',
            name='messagetopost',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='messages',
            name='subject',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='onlinetest',
            name='questionname',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='onlinetestanswers',
            name='answertext',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='onlinetestquestionoption',
            name='optionname',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='onlinetestresults',
            name='answertext',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='options',
            name='optionname',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='accountno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='iban',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='slipurl',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='paymentconfirmation',
            name='transactionslipnumber',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='post',
            name='posttext',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='posttitle',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='quizcontext',
            name='question',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='quizcontextresult',
            name='answertext',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='replies',
            name='replyform',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='replies',
            name='replymessage',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='resultclient',
            name='answertext',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='rolename',
            name='rolename',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='school',
            name='schoolemail',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='school',
            name='schoolname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='schoolassignment',
            name='assignmentname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='schoolassignment',
            name='assignmenturl',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='status',
            name='statustype',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='contactno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='regno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentcomplain',
            name='complaindescription',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='studentcomplain',
            name='replymsg',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='studenthistory',
            name='lastclass',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='studenthistory',
            name='lastclasssection',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='studentmaster',
            name='classname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='studentmaster',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='studentmaster',
            name='sectionname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='studentresult',
            name='percentage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='submitassignment',
            name='uploadurl',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='submitmanualtest',
            name='uploadurl',
            field=models.URLField(max_length=150),
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='subemail',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='superadmin',
            name='ademail',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='superadmin',
            name='adimageurl',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='superadmin',
            name='adname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tblclass',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='team',
            name='longdescription',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='team',
            name='shortdescription',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='technictip',
            name='longdes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='technictip',
            name='shortdes',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='technictip',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='technictip',
            name='videopath',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='allocationstatus',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='userenrollincourse',
            name='registrationid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userfeedback',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='webadd',
            name='link',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='websitereview',
            name='comment',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='websitereview',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='websitereview',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='parents',
            name='assignmentid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.SchoolAssignment'),
        ),
        migrations.AddField(
            model_name='parents',
            name='studentid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.Attendance'),
        ),
        migrations.AddField(
            model_name='parents',
            name='studentresultid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.StudentResult'),
        ),
    ]