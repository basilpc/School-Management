# Generated by Django 4.1.5 on 2023-01-23 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_rename_marklist_mark_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark_list',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='mark_list',
            name='s10',
        ),
        migrations.RemoveField(
            model_name='mark_list',
            name='s6',
        ),
        migrations.RemoveField(
            model_name='mark_list',
            name='s7',
        ),
        migrations.RemoveField(
            model_name='mark_list',
            name='s8',
        ),
        migrations.RemoveField(
            model_name='mark_list',
            name='s9',
        ),
    ]