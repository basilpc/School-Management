# Generated by Django 4.1.5 on 2023-02-01 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0023_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Teaching_subjects',
        ),
        migrations.AddField(
            model_name='user',
            name='Subject',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='student.subject'),
        ),
    ]
