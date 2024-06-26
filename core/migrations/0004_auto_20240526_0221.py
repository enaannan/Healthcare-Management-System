# Generated by Django 5.0.6 on 2024-05-26 02:21

from django.db import migrations

from core.models.role import Role


def create_roles(apps, schema_editor):
    for role in Role.OfficerRoles.choices:
        Role.objects.get_or_create(name=role[0])

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_role_role_name_role_name'),
    ]

    operations = [
        migrations.RunPython(create_roles),
    ]