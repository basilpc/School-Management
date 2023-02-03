# Generated by Django 4.1.5 on 2023-01-21 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_subjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='marklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.subjects')),
            ],
        ),
    ]
