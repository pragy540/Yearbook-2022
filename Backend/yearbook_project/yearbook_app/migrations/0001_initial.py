# Generated by Django 3.2.7 on 2022-02-16 16:25

from django.db import migrations, models
import django.db.models.deletion
import yearbook_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alum',
            fields=[
                ('sso_id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, validators=[yearbook_app.models.validate_email_iitb_domain])),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sso_id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('first_name', models.CharField(db_index=True, default='', max_length=255)),
                ('last_name', models.CharField(blank=True, db_index=True, default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, validators=[yearbook_app.models.validate_email_iitb_domain])),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('personal_email', models.EmailField(default='personal@gmail.com', max_length=254)),
                ('dob', models.DateField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('hostel', models.CharField(choices=[('1', 'Hostel 1'), ('2', 'Hostel 2'), ('3', 'Hostel 3'), ('4', 'Hostel 4'), ('5', 'Hostel 5'), ('6', 'Hostel 6'), ('7', 'Hostel 7'), ('8', 'Hostel 8'), ('9', 'Hostel 9'), ('10', 'Hostel 10'), ('11', 'Hostel 11'), ('12', 'Hostel 12'), ('13', 'Hostel 13'), ('14', 'Hostel 14'), ('15', 'Hostel 15'), ('16', 'Hostel 16'), ('17', 'Hostel 17'), ('18', 'Hostel 18'), ('tansa', 'Hostel Tansa'), ('qip', 'QIP')], max_length=255, null=True)),
                ('room_no', models.CharField(blank=True, default='101', max_length=10, null=True)),
                ('department', models.CharField(choices=[('Aerospace Engineering', 'Aerospace Engineering'), ('Animation', 'Animation'), ('Application Software Centre', 'Application Software Centre'), ('Applied Geophysics', 'Applied Geophysics'), ('Applied Statistics and Informatics', 'Applied Statistics and Informatics'), ('Biomedical Engineering', 'Biomedical Engineering'), ('Biosciences and Bioengineering', 'Biosciences and Bioengineering'), ('Biotechnology', 'Biotechnology'), ('Centre for Aerospace Systems Design and Engineering', 'Centre for Aerospace Systems Design and Engineering'), ('Centre for Distance Engineering Education Programme', 'Centre for Distance Engineering Education Programme'), ('Centre for Environmental Science and Engineering', 'Centre for Environmental Science and Engineering'), ('Centre for Formal Design and Verification of Software', 'Centre for Formal Design and Verification of Software'), ('Centre for Research in Nanotechnology and Science', 'Centre for Research in Nanotechnology and Science'), ('Centre for Technology Alternatives for Rural Areas', 'Centre for Technology Alternatives for Rural Areas'), ('Centre for Urban Science and Engineering', 'Centre for Urban Science and Engineering'), ('Centre of Studies in Resources Engineering', 'Centre of Studies in Resources Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Chemistry', 'Chemistry'), ('Civil Engineering', 'Civil Engineering'), ('Climate Studies', 'Climate Studies'), ('Computer Centre', 'Computer Centre'), ('Computer Science & Engineering', 'Computer Science & Engineering'), ('Continuing Education Programme', 'Continuing Education Programme'), ('Corrosion Science and Engineering', 'Corrosion Science and Engineering'), ('Desai Sethi Centre for Entrepreneurship', 'Desai Sethi Centre for Entrepreneurship'), ('Earth Sciences', 'Earth Sciences'), ('Educational Technology', 'Educational Technology'), ('Electrical Engineering', 'Electrical Engineering'), ('Energy Science and Engineering', 'Energy Science and Engineering'), ('Economics (HSS)', 'Economics (HSS)'), ('Engineering Physics', 'Engineering Physics'), ('Humanities & Social Science', 'Humanities & Social Science'), ('IITB-Monash Research Academy', 'IITB-Monash Research Academy'), ('Industrial Design Centre', 'Industrial Design Centre'), ('Industrial Engineering and Operations Research', 'Industrial Engineering and Operations Research'), ('Industrial Management', 'Industrial Management'), ('Interaction Design', 'Interaction Design'), ('Kanwal Rekhi School of Information Technology', 'Kanwal Rekhi School of Information Technology'), ('Material Science', 'Material Science'), ('Materials, Manufacturing and Modelling', 'Materials, Manufacturing and Modelling'), ('Mathematics', 'Mathematics'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Metallurgical Engineering & Materials Science', 'Metallurgical Engineering & Materials Science'), ('Mobility and Vehicle Design', 'Mobility and Vehicle Design'), ('National Centre for Aerospace Innovation and Research', 'National Centre for Aerospace Innovation and Research'), ('National Centre for Mathematics', 'National Centre for Mathematics'), ('Physical Education', 'Physical Education'), ('Physics', 'Physics'), ('Physics, Material Science', 'Physics, Material Science'), ('Preparatory Course', 'Preparatory Course'), ('Reliability Engineering', 'Reliability Engineering'), ('Shailesh J. Mehta School of Management', 'Shailesh J. Mehta School of Management'), ('Sophisticated Analytical Instrument Facility', 'Sophisticated Analytical Instrument Facility'), ('Systems and Control Engineering', 'Systems and Control Engineering'), ('Tata Center for Technology and Design', 'Tata Center for Technology and Design'), ('Technology and Development', 'Technology and Development'), ('Visual Communication', 'Visual Communication'), ('Wadhwani Research Centre for Bioengineering', 'Wadhwani Research Centre for Bioengineering'), ('Centre for Policy Studies', 'Centre for Policy Studies')], max_length=255, null=True)),
                ('program', models.CharField(choices=[('ug', 'Undergraduate'), ('dd', 'Dual Degree'), ('pg', 'Postgraduate'), ('idddp', 'Inter-Disciplinary Dual Degree')], max_length=30, null=True)),
                ('degree', models.CharField(choices=[('FYBS', 'Four Year BS'), ('BTECH', 'Bachelor of Technology'), ('MTECH', 'Master of Technology'), ('DD', 'B.Tech. + M.Tech. Dual Degree'), ('MSC', 'Master of Science'), ('PHD', 'Doctor of Philosophy'), ('BDES', 'Bachelor of Design'), ('MDES', 'Master of Design'), ('MPHIL', 'Master of Philosophy'), ('MMG', 'Master of Management'), ('MSEx', 'M.S. (Exit Degree)'), ('MtechEx', 'Master of Technology (Exit Degree)'), ('MtechPhDDD', 'M.Tech. + Ph.D. Dual Degree'), ('PC', 'Preparatory Course'), ('VS', 'Visiting Student'), ('MPhilEx', 'Master of Philosophy (Exit Degree)'), ('MScEx', 'Master of Science (Exit Degree)'), ('MScMTechDD', 'M.Sc. + M.Tech. Dual Degree'), ('MScPhDDD', 'M.Sc. + Ph.D. Dual Degree'), ('MPhilPhDDD', 'M.Phil. + Ph.D. Dual Degree'), ('EMBA', 'Executive MBA'), ('IMTECH', 'Integrated M.Tech.'), ('MSCBR', 'Master of Science By Research'), ('TYMSC', 'Two Year M.Sc.'), ('FYIMSC', 'Five Year Integrated M.Sc.'), ('DIIT', 'D.I.I.T.'), ('DIITEx', 'D.I.T.T. (Exit Degree)')], max_length=50, null=True)),
                ('join_year', models.IntegerField(default=2017, null=True)),
                ('graduation_year', models.IntegerField(default=2021, null=True)),
                ('nickname', models.CharField(blank=True, max_length=25, null=True)),
                ('tagline', models.CharField(blank=True, max_length=110, null=True)),
                ('ib1', models.CharField(blank=True, max_length=255, null=True)),
                ('ib2', models.CharField(blank=True, max_length=255, null=True)),
                ('ib3', models.CharField(blank=True, max_length=255, null=True)),
                ('img1', models.ImageField(blank=True, null=True, upload_to='')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='')),
                ('img4', models.ImageField(blank=True, null=True, upload_to='')),
                ('question1', models.CharField(blank=True, choices=[('pastself', 'If you get the chance to meet freshie self again, what is that one thing you will tell him or her?'), ('movie', 'You become famous and someone wants to film a movie on your college life, what will it be called?'), ('neverever', 'In my insti life, Never have I Ever:'), ('memories', 'If you could pack up a bunch of things from the institute to keep with you forever, what will those be?')], max_length=100, null=True)),
                ('answer1', models.TextField(blank=True, max_length=300, null=True)),
                ('notification_preference', models.IntegerField(blank=True, choices=[(0, 'Do not send any notifications'), (1, 'Send Only if someone writes on my wall'), (2, "In addition to above, Send if I'm tagged in a post"), (3, 'In addition to above, Send if someone tags me in a Impression'), (4, 'Send Everytime someone tags me or writes for me or comments on my post')], default=1, null=True)),
                ('details_done', models.BooleanField(default=False)),
                ('student', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='yearbook_app.student')),
            ],
        ),
    ]
