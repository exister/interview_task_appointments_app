# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def forwards_func(apps, schema_editor):
    Doctor = apps.get_model("core", "Doctor")
    Doctor.objects.bulk_create([
        Doctor(last_name='Пупкин', first_name='Василий', middle_name='Иванович'),
        Doctor(last_name='Иваноп', first_name='Петр', middle_name='Петрович'),
    ])


def reverse_func(apps, schema_editor):
    Doctor = apps.get_model("core", "Doctor")
    Doctor.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
