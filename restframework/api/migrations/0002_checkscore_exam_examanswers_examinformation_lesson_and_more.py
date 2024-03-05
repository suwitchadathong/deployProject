# Generated by Django 4.2.5 on 2023-11-26 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkscore',
            fields=[
                ('scoreid', models.AutoField(db_column='ScoreID', primary_key=True, serialize=False)),
                ('activatekey_score', models.TextField(blank=True, db_column='ActivateKey_Score', null=True)),
            ],
            options={
                'db_table': 'checkscore',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('examid', models.AutoField(db_column='ExamID', primary_key=True, serialize=False)),
                ('nameexam', models.TextField(blank=True, db_column='NameExam', null=True)),
                ('examno', models.IntegerField(blank=True, db_column='ExamNo', null=True)),
                ('numexam', models.IntegerField(blank=True, db_column='NumExam', null=True)),
                ('setexam', models.IntegerField(blank=True, db_column='SetExam', null=True)),
                ('imganswers_format_path', models.TextField(blank=True, db_column='ImgAnswerS_format_path', null=True)),
                ('std_csv_path', models.TextField(blank=True, db_column='Std_csv_path', null=True)),
            ],
            options={
                'db_table': 'exam',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Examanswers',
            fields=[
                ('examanswersid', models.AutoField(db_column='ExamAnswersID', primary_key=True, serialize=False)),
                ('setexamans', models.IntegerField(blank=True, db_column='SetExamAns', null=True)),
                ('scoringcriteria', models.TextField(blank=True, db_column='ScoringCriteria', null=True)),
                ('papeans_path', models.TextField(blank=True, db_column='PapeAns_path', null=True)),
            ],
            options={
                'db_table': 'examanswers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Examinformation',
            fields=[
                ('examinfoid', models.AutoField(db_column='ExaminfoID', primary_key=True, serialize=False)),
                ('stdid', models.CharField(blank=True, db_column='StdID', max_length=20, null=True)),
                ('subidstd', models.CharField(blank=True, db_column='SubIDStd', max_length=20, null=True)),
                ('examseatnumber', models.CharField(blank=True, db_column='ExamSeatNumber', max_length=20, null=True)),
                ('setexaminfo', models.IntegerField(blank=True, db_column='SetExamInfo', null=True)),
                ('section', models.CharField(blank=True, db_column='Section', max_length=20, null=True)),
                ('score', models.IntegerField(blank=True, db_column='Score', null=True)),
                ('correct', models.IntegerField(blank=True, db_column='Correct', null=True)),
                ('wrong', models.IntegerField(blank=True, db_column='Wrong', null=True)),
                ('unresponsive', models.IntegerField(blank=True, db_column='Unresponsive', null=True)),
                ('anschoicestd', models.TextField(blank=True, db_column='AnsChoiceStd', null=True)),
                ('activatekey_exan', models.CharField(blank=True, db_column='ActivateKey_Exan', max_length=100, null=True)),
                ('imgansstd_path', models.TextField(blank=True, db_column='ImgAnsStd_path', null=True)),
            ],
            options={
                'db_table': 'examinformation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('lessonid', models.AutoField(db_column='LessonID', primary_key=True, serialize=False)),
                ('namelesson', models.TextField(blank=True, db_column='NameLesson', null=True)),
                ('infolesson', models.TextField(blank=True, db_column='InfoLesson', null=True)),
            ],
            options={
                'db_table': 'lesson',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lessonanswer',
            fields=[
                ('lessonandanswer', models.AutoField(db_column='LessonAndAnswer', primary_key=True, serialize=False)),
                ('choicelesson', models.TextField(blank=True, db_column='ChoiceLesson', null=True)),
            ],
            options={
                'db_table': 'lessonanswer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Queheaddetails',
            fields=[
                ('queheaddetailsid', models.AutoField(db_column='QueHeadDetailsID', primary_key=True, serialize=False)),
                ('quehead1', models.TextField(blank=True, db_column='QueHead1', null=True)),
                ('quehead2', models.TextField(blank=True, db_column='QueHead2', null=True)),
                ('quehead3', models.TextField(blank=True, db_column='QueHead3', null=True)),
                ('quehead4', models.TextField(blank=True, db_column='QueHead4', null=True)),
                ('quehead5', models.TextField(blank=True, db_column='QueHead5', null=True)),
            ],
            options={
                'db_table': 'queheaddetails',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Queinformation',
            fields=[
                ('queinfoid', models.AutoField(db_column='QueinfoID', primary_key=True, serialize=False)),
                ('ansquehead', models.TextField(blank=True, db_column='AnsQueHead', null=True)),
                ('ansquetopic', models.TextField(blank=True, db_column='AnsQueTopic', null=True)),
                ('imgansstd_path', models.TextField(blank=True, db_column='ImgAnsStd_path', null=True)),
                ('status_queinfo', models.CharField(blank=True, db_column='Status_QueInfo', max_length=10, null=True)),
            ],
            options={
                'db_table': 'queinformation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Quesheet',
            fields=[
                ('quesheetid', models.AutoField(db_column='QueSheetID', primary_key=True, serialize=False)),
                ('quesheetname', models.TextField(blank=True, db_column='QueSheetName', null=True)),
                ('quesheettopicname', models.TextField(blank=True, db_column='QueSheetTopicName', null=True)),
                ('detailslineone', models.TextField(blank=True, db_column='DetailsLineOne', null=True)),
                ('detailslinetwo', models.TextField(blank=True, db_column='DetailsLinetwo', null=True)),
                ('explanation', models.TextField(blank=True, db_column='Explanation', null=True)),
                ('symbolposition', models.CharField(blank=True, db_column='Symbolposition', max_length=10, null=True)),
                ('imglogoquesheet_path', models.TextField(blank=True, db_column='ImgLogoQueSheet_path', null=True)),
                ('imgquesheet_path', models.TextField(blank=True, db_column='ImgQueSheet_path', null=True)),
                ('activatekey_que', models.TextField(blank=True, db_column='ActivateKey_Que', null=True)),
                ('datetimestart', models.DateTimeField(blank=True, db_column='DateTimeStart', null=True)),
                ('datetimeend', models.DateTimeField(blank=True, db_column='DateTimeEnd', null=True)),
                ('statusquesheet', models.CharField(blank=True, db_column='StatusQueSheet', max_length=10, null=True)),
            ],
            options={
                'db_table': 'quesheet',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Quetopicdetails',
            fields=[
                ('quetopicdetailsid', models.AutoField(db_column='QueTopicDetailsID', primary_key=True, serialize=False)),
                ('quetopicnum', models.TextField(blank=True, db_column='QueTopicNum', null=True)),
                ('quetopicdetails', models.TextField(blank=True, db_column='QueTopicDetails', null=True)),
                ('quetopicformat', models.TextField(blank=True, db_column='QueTopicFormat', null=True)),
                ('quetopictype', models.TextField(blank=True, db_column='QueTopicType', null=True)),
            ],
            options={
                'db_table': 'quetopicdetails',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('requestid', models.AutoField(db_column='RequestID', primary_key=True, serialize=False)),
                ('imgrequest_path', models.TextField(blank=True, db_column='ImgRequest_path', null=True)),
                ('status_request', models.IntegerField(blank=True, db_column='Status_Request', null=True)),
            ],
            options={
                'db_table': 'request',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('typesid', models.AutoField(db_column='TypesID', primary_key=True, serialize=False)),
                ('typesname', models.CharField(blank=True, db_column='TypesName', max_length=40, null=True)),
                ('limitsub', models.IntegerField(blank=True, db_column='LimitSub', null=True)),
                ('limitque', models.IntegerField(blank=True, db_column='LimitQue', null=True)),
            ],
            options={
                'db_table': 'role',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subid', models.AutoField(db_column='SubID', primary_key=True, serialize=False)),
                ('subjectid', models.CharField(blank=True, db_column='SubjectID', max_length=20, null=True)),
                ('subname', models.CharField(blank=True, db_column='SubName', max_length=100, null=True)),
                ('year', models.CharField(blank=True, db_column='Year', max_length=10, null=True)),
                ('semester', models.CharField(blank=True, db_column='Semester', max_length=10, null=True)),
            ],
            options={
                'db_table': 'subject',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sublesson',
            fields=[
                ('sublessonid', models.AutoField(db_column='SubLessonID', primary_key=True, serialize=False)),
                ('numlesson', models.TextField(blank=True, db_column='NumLesson', null=True)),
                ('namelesson', models.TextField(blank=True, db_column='NameLesson', null=True)),
                ('infolesson', models.TextField(blank=True, db_column='InfoLesson', null=True)),
            ],
            options={
                'db_table': 'sublesson',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(db_column='UserID', primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=100, null=True)),
                ('fullname', models.TextField(blank=True, db_column='FullName', null=True)),
                ('password', models.CharField(blank=True, db_column='Password', max_length=60, null=True)),
                ('googleid', models.TextField(blank=True, db_column='googleId', null=True)),
                ('job', models.TextField(blank=True, db_column='Job', null=True)),
                ('department', models.TextField(blank=True, db_column='Department', null=True)),
                ('faculty', models.TextField(blank=True, db_column='Faculty', null=True)),
                ('workplace', models.TextField(blank=True, db_column='Workplace', null=True)),
                ('tel', models.CharField(blank=True, db_column='Tel', max_length=10, null=True)),
                ('usageformat', models.CharField(blank=True, db_column='Usageformat', max_length=10, null=True)),
                ('imge_kyc_path', models.TextField(blank=True, db_column='ImgE_KYC_path', null=True)),
                ('e_kyc', models.CharField(blank=True, db_column='E_KYC', max_length=20, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]