# Generated by Django 4.1.5 on 2023-01-23 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_mark_list_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark_list',
            name='user_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]