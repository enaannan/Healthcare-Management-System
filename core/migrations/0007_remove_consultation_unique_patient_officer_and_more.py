# Generated by Django 5.0.6 on 2024-05-28 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_consultation_officer_consultation_practitioner'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='consultation',
            name='unique_patient_officer',
        ),
        migrations.RemoveField(
            model_name='consultation',
            name='notes',
        ),
        migrations.AddConstraint(
            model_name='consultation',
            constraint=models.UniqueConstraint(fields=('patient', 'practitioner'), name='unique_patient_practitioner'),
        ),
    ]
