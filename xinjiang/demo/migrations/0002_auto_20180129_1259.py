# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='apartment',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='family_allIn',
            field=models.CharField(default=None, max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='family_person_number',
            field=models.IntegerField(default=None, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='family_pool',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='student',
            name='graduate_highSchool',
            field=models.CharField(default=None, max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='high_test_grade',
            field=models.IntegerField(default=None, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='immigration_document_number',
            field=models.IntegerField(default=None, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='immigration_document_type',
            field=models.CharField(default=None, max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='martyr_son',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='student',
            name='no_parents',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='student',
            name='only_child',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='student',
            name='parents',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='student',
            name='parents_noe_work',
            field=models.CharField(default=None, max_length=300),
        ),
        migrations.AddField(
            model_name='student',
            name='parents_one_birthday',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='student',
            name='parents_one_body',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='student',
            name='parents_one_duty',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='student',
            name='parents_one_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='parents_one_phone_number',
            field=models.BigIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='student',
            name='parents_one_political_status',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='parents_one_relationship',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='parents_two_birthday',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='student',
            name='parents_two_body',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='student',
            name='parents_two_duty',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='student',
            name='parents_two_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='parents_two_phone_number',
            field=models.BigIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='student',
            name='parents_two_political_status',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='parents_two_relationship',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='parents_two_work',
            field=models.CharField(default=None, max_length=300),
        ),
        migrations.AddField(
            model_name='student',
            name='party_membership_application',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='student',
            name='party_number',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='student',
            name='pool',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='student',
            name='pool_reason',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='student',
            name='study_mode_before_college',
            field=models.CharField(default=None, max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='teacher_name',
            field=models.CharField(default=None, max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='teacher_phone_number',
            field=models.BigIntegerField(default=None, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='telephone_number',
            field=models.IntegerField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Class',
            field=models.IntegerField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='family_address',
            field=models.TextField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='from_beforeStudy',
            field=models.TextField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='id_card',
            field=models.BigIntegerField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='politics_status',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='study',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='study_class',
            field=models.TextField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='study_system',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
