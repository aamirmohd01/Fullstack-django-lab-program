# Generated by Django 5.0.6 on 2024-06-15 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=40)),
                ('course_name', models.CharField(max_length=100)),
                ('course_credit', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_usn', models.CharField(max_length=20)),
                ('student_name', models.CharField(max_length=100)),
                ('student_sem', models.IntegerField()),
                ('enrolment', models.ManyToManyField(to='app8.course')),
            ],
        ),
    ]
