# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ermsapp.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CV_Status',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Degree', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Degree_class',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Class', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Degree_For_Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Degree', models.ForeignKey(to='ermsapp.Degree')),
            ],
        ),
        migrations.CreateModel(
            name='DegreeField',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Field', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DegreeType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Type', models.CharField(max_length=10)),
                ('HierachyNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('DeptName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Exp_Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Duration', models.FloatField(max_length=2.2)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('AltPost', models.CharField(blank=True, null=True, max_length=100)),
                ('Field', models.CharField(max_length=100)),
                ('Duration', models.FloatField(max_length=2.2)),
                ('Notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Extracurricular',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Extracurricular', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Time', models.TimeField()),
                ('Date', models.DateField()),
                ('Interviewer_Review', models.TextField(blank=True, null=True)),
                ('HOD_Review', models.TextField(blank=True, null=True)),
                ('HR_Review', models.TextField(blank=True, null=True)),
                ('NoOfPasses', models.PositiveIntegerField()),
                ('NoOfFails', models.PositiveIntegerField()),
                ('NoOfOnHolds', models.PositiveIntegerField()),
                ('Department', models.ForeignKey(to='ermsapp.Department')),
                ('HOD', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InterviewType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('InterviewType', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Message_Recieve',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('RecievedDate', models.DateField()),
                ('RecievedTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Message_Send',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('SentDate', models.DateField()),
                ('SentTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('MsgType', models.IntegerField()),
                ('MsgCont', models.TextField(blank=True, null=True)),
                ('MsgAcceptance', models.IntegerField()),
                ('Reciever', models.ManyToManyField(related_name='Reciever_User', to=settings.AUTH_USER_MODEL, through='ermsapp.Message_Recieve')),
                ('Sender', models.ManyToManyField(related_name='Sender_User', to=settings.AUTH_USER_MODEL, through='ermsapp.Message_Send')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('NIC', models.CharField(max_length=12, unique=True)),
                ('FName', models.CharField(max_length=30)),
                ('LName', models.CharField(max_length=30)),
                ('FullName', models.CharField(max_length=100)),
                ('DOB', models.DateField(null=True)),
                ('Nationality', models.CharField(max_length=20)),
                ('AddressLine1', models.CharField(max_length=100)),
                ('AddressLine2', models.CharField(max_length=100)),
                ('AddressLine3', models.CharField(max_length=100)),
                ('AddressLine4', models.CharField(blank=True, null=True, max_length=100)),
                ('ContactNum', models.CharField(max_length=12)),
                ('Email', models.EmailField(blank=True, null=True, max_length=254)),
                ('FacebookProf', models.CharField(blank=True, null=True, max_length=100)),
                ('LinkedInProf', models.CharField(blank=True, null=True, max_length=100)),
                ('PImage', models.FileField(blank=True, null=True, upload_to=ermsapp.models.Person_directory_path)),
                ('Objective', models.TextField(blank=True, null=True)),
                ('CVPDF', models.FileField(blank=True, null=True, upload_to=ermsapp.models.Person_directory_path)),
                ('SpecialNotes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person_Degree',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Year', models.DateField()),
                ('SpecialNotes', models.TextField(null=True)),
                ('Class', models.ForeignKey(to='ermsapp.Degree_class', blank=True, null=True)),
                ('Degree', models.ForeignKey(to='ermsapp.Degree')),
                ('Person', models.ForeignKey(to='ermsapp.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Person_Interview',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Interview', models.ForeignKey(to='ermsapp.Interview')),
                ('Person', models.ForeignKey(to='ermsapp.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Person_Interview_viewer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Comment', models.TextField()),
                ('Rate', models.PositiveSmallIntegerField()),
                ('Person_Interview', models.ForeignKey(to='ermsapp.Person_Interview')),
                ('Status', models.ForeignKey(to='ermsapp.CV_Status')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Post', models.CharField(max_length=100)),
                ('Field', models.CharField(blank=True, null=True, max_length=100)),
                ('NoOfInterviews', models.PositiveIntegerField()),
                ('InterviewType', models.ManyToManyField(to='ermsapp.InterviewType')),
                ('degree', models.ManyToManyField(to='ermsapp.Degree', through='ermsapp.Degree_For_Post')),
            ],
        ),
        migrations.CreateModel(
            name='Post_Dept',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Dept', models.ForeignKey(to='ermsapp.Department')),
                ('Post', models.ForeignKey(to='ermsapp.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Skill', models.TextField()),
                ('person', models.ForeignKey(to='ermsapp.Person')),
            ],
        ),
        migrations.CreateModel(
            name='SpecialAchievements',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Heading_1', models.CharField(max_length=100)),
                ('Heading_2', models.CharField(max_length=100)),
                ('Notes', models.TextField()),
                ('Person', models.ForeignKey(to='ermsapp.Person')),
            ],
        ),
        migrations.CreateModel(
            name='SpecializedArea',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('SpecializedArea', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Sports', models.TextField()),
                ('person', models.ForeignKey(to='ermsapp.Person')),
            ],
        ),
        migrations.CreateModel(
            name='SubQualification',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('QName', models.CharField(max_length=100)),
                ('Subject', models.CharField(max_length=150)),
                ('Result', models.CharField(blank=True, null=True, max_length=10)),
                ('SubResult', models.CharField(max_length=4)),
                ('QType', models.IntegerField()),
                ('SpecialNotes', models.TextField(blank=True, null=True)),
                ('person', models.ForeignKey(to='ermsapp.Person')),
            ],
        ),
        migrations.CreateModel(
            name='subQul_Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('QName', models.CharField(max_length=100)),
                ('SubResult', models.CharField(max_length=10)),
                ('Post', models.ForeignKey(to='ermsapp.Post')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('university', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Role', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('FullName', models.CharField(max_length=100)),
                ('UPhoto', models.FileField(blank=True, null=True, upload_to=ermsapp.models.User_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('DateOfPublish', models.DateField()),
                ('ClosingDate', models.DateField()),
                ('NoOfIntDone', models.IntegerField()),
                ('NoOfPossitions', models.IntegerField()),
                ('DeptID', models.ForeignKey(to='ermsapp.Department')),
                ('Post', models.ForeignKey(to='ermsapp.Post')),
                ('Post_Dept', models.ForeignKey(to='ermsapp.Post_Dept')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('HallName', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Interviewers',
            fields=[
                ('users_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='ermsapp.Users', serialize=False, parent_link=True)),
                ('NoOfInts', models.PositiveIntegerField(blank=True, null=True)),
            ],
            bases=('ermsapp.users',),
        ),
        migrations.AddField(
            model_name='users',
            name='Department',
            field=models.ForeignKey(to='ermsapp.Department'),
        ),
        migrations.AddField(
            model_name='users',
            name='Post',
            field=models.ForeignKey(to='ermsapp.Post'),
        ),
        migrations.AddField(
            model_name='users',
            name='User',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='users',
            name='UserRole',
            field=models.ForeignKey(to='ermsapp.UserRole'),
        ),
        migrations.AddField(
            model_name='person',
            name='Degree',
            field=models.ManyToManyField(to='ermsapp.Degree', through='ermsapp.Person_Degree'),
        ),
        migrations.AddField(
            model_name='person',
            name='Department',
            field=models.ManyToManyField(to='ermsapp.Department'),
        ),
        migrations.AddField(
            model_name='person',
            name='Interview',
            field=models.ManyToManyField(to='ermsapp.Interview', through='ermsapp.Person_Interview'),
        ),
        migrations.AddField(
            model_name='person',
            name='Post',
            field=models.ManyToManyField(to='ermsapp.Post'),
        ),
        migrations.AddField(
            model_name='message_send',
            name='Messages',
            field=models.ForeignKey(to='ermsapp.Messages'),
        ),
        migrations.AddField(
            model_name='message_send',
            name='Sender',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message_recieve',
            name='Messages',
            field=models.ForeignKey(to='ermsapp.Messages'),
        ),
        migrations.AddField(
            model_name='message_recieve',
            name='Reciever',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='interview',
            name='InterviewType',
            field=models.ForeignKey(to='ermsapp.InterviewType'),
        ),
        migrations.AddField(
            model_name='interview',
            name='Interviewers',
            field=models.ManyToManyField(related_name='User_Interviewer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='interview',
            name='Vacancy',
            field=models.ForeignKey(to='ermsapp.Vacancy'),
        ),
        migrations.AddField(
            model_name='interview',
            name='Venue',
            field=models.ForeignKey(to='ermsapp.Venue'),
        ),
        migrations.AddField(
            model_name='extracurricular',
            name='person',
            field=models.ForeignKey(to='ermsapp.Person'),
        ),
        migrations.AddField(
            model_name='experience',
            name='Person',
            field=models.ForeignKey(to='ermsapp.Person'),
        ),
        migrations.AddField(
            model_name='experience',
            name='Post',
            field=models.ForeignKey(to='ermsapp.Post', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exp_post',
            name='ExPost',
            field=models.ForeignKey(related_name='ExPost', to='ermsapp.Post'),
        ),
        migrations.AddField(
            model_name='exp_post',
            name='Post',
            field=models.ForeignKey(to='ermsapp.Post'),
        ),
        migrations.AddField(
            model_name='degree_for_post',
            name='Post',
            field=models.ForeignKey(to='ermsapp.Post'),
        ),
        migrations.AddField(
            model_name='degree',
            name='DegreeField',
            field=models.ForeignKey(to='ermsapp.DegreeField'),
        ),
        migrations.AddField(
            model_name='degree',
            name='DegreeType',
            field=models.ForeignKey(to='ermsapp.DegreeType'),
        ),
        migrations.AddField(
            model_name='degree',
            name='University',
            field=models.ForeignKey(to='ermsapp.University'),
        ),
        migrations.AddField(
            model_name='person_interview_viewer',
            name='Interviewers',
            field=models.ForeignKey(to='ermsapp.Interviewers'),
        ),
        migrations.AddField(
            model_name='person_interview',
            name='Interviewers',
            field=models.ManyToManyField(to='ermsapp.Interviewers', through='ermsapp.Person_Interview_viewer'),
        ),
        migrations.AddField(
            model_name='interviewers',
            name='Interview',
            field=models.ManyToManyField(to='ermsapp.Interview'),
        ),
        migrations.AddField(
            model_name='interviewers',
            name='SpecializedArea',
            field=models.ManyToManyField(to='ermsapp.SpecializedArea'),
        ),
    ]
