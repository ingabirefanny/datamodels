# Generated by Django 5.0.6 on 2024-08-20 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('student', '0002_courses_student_courses'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Courses',
        ),
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='course.course'),
        ),
    ]