# Generated by Django 4.1.5 on 2023-01-23 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_remove_marklist_subject_marklist_grade_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='marklist',
            new_name='mark_list',
        ),
    ]