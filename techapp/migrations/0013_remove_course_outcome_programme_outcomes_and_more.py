# Generated by Django 4.2.7 on 2024-03-15 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techapp', '0012_course_outcome_programme_outcomes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_outcome',
            name='programme_outcomes',
        ),
        migrations.RemoveField(
            model_name='course_outcome',
            name='programme_specific_outcomes',
        ),
    ]
