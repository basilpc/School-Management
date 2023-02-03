# Generated by Django 4.1.5 on 2023-01-19 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_user_gender_alter_user_roll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='roll',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Teacher', 'Teacher'), ('Student', 'Student')], max_length=100, null=True),
        ),
    ]
