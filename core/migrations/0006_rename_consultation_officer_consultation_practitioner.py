# Generated by Django 5.0.6 on 2024-05-28 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_role_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consultation',
            old_name='consultation_officer',
            new_name='practitioner',
        ),
    ]