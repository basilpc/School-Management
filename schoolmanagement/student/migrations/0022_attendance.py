# Generated by Django 4.1.5 on 2023-01-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0021_user_is_tutor_alter_user_teaching_subjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100, null=True)),
                ('standard', models.CharField(max_length=100, null=True)),
                ('date', models.CharField(max_length=100, null=True)),
                ('attendance', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
