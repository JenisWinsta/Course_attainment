# Generated by Django 4.2.7 on 2024-03-13 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techapp', '0011_course_outcome_programme_specific_outcomes'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_outcome',
            name='programme_outcomes',
            field=models.ManyToManyField(to='techapp.programme_outcome'),
        ),
    ]
