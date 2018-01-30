# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('name', models.CharField(max_length=10)),
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('sex', models.CharField(max_length=10)),
                ('id_card', models.IntegerField(default=None)),
                ('family_address', models.TextField(default=None)),
                ('study_class', models.TextField(default=None)),
                ('study', models.CharField(max_length=100)),
                ('Class', models.IntegerField(default=None)),
                ('group', models.CharField(max_length=30)),
                ('from_beforeStudy', models.TextField(default=None)),
                ('study_system', models.CharField(max_length=50)),
                ('politics_status', models.CharField(max_length=100)),
            ],
        ),
    ]
