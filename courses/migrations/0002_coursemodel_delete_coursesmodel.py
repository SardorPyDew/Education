# Generated by Django 5.1 on 2024-08-22 19:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('mentor', models.ForeignKey(limit_choices_to={'role': 'Mentor'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mentor_course', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(limit_choices_to={'role': 'User'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_course', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='CoursesModel',
        ),
    ]