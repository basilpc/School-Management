# Generated by Django 4.1.5 on 2023-01-19 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_alter_user_gender_alter_user_roll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='standard',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
