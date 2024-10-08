# Generated by Django 5.0.6 on 2024-06-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('year_of_birth', models.DateField(max_length=10)),
                ('nationality', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=30)),
                ('teacher_id', models.PositiveSmallIntegerField()),
                ('course', models.CharField(max_length=20)),
                ('years_of_experience', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
