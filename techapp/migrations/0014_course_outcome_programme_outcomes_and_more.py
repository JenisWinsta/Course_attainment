# Generated by Django 4.2.7 on 2024-03-15 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techapp', '0013_remove_course_outcome_programme_outcomes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_outcome',
            name='programme_outcomes',
            field=models.ManyToManyField(to='techapp.programme_outcome'),
        ),
        migrations.AddField(
            model_name='course_outcome',
            name='programme_specific_outcomes',
            field=models.ManyToManyField(to='techapp.programme_specific_outcome'),
        ),
    ]
