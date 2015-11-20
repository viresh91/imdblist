# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='id',
        ),
        migrations.AlterField(
            model_name='movies',
            name='name',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
    ]
