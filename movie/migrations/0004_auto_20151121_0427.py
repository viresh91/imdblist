# -*- coding: utf-8 -*-
from django.db import models, migrations

def apply_migration(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.bulk_create([
        Group(name=u'admin'),
        Group(name=u'user'),
    ])


def revert_migration(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(
        name__in=[
            u'admin',
            u'user',
        ]
    ).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20151119_1746'),
    ]

    operations = [
        migrations.RunPython(apply_migration, revert_migration),
    ]