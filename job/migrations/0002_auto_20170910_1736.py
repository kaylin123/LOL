# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-10 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nm_stepinstance',
            name='ipListId',
        ),
        migrations.AlterField(
            model_name='nm_iplist',
            name='stepInstance_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='job.Nm_StepInstance', verbose_name='\u6267\u884c\u4f5c\u4e1a\u5b9e\u4f8b\u6b65\u9aa4id'),
        ),
    ]
