# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-08-30 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, unique=True, verbose_name='\u540d\u79f0')),
                ('appId', models.CharField(max_length=255, null=True, verbose_name='\u5f00\u53d1\u5546id')),
                ('TYPE', models.IntegerField(blank=True, default=1, null=True, verbose_name='\u7c7b\u578b')),
                ('isPublic', models.BooleanField(default=True, verbose_name='\u662f\u5426\u516c\u5171\u811a\u672c')),
                ('content', models.TextField(blank=True, null=True, verbose_name='\u811a\u672c\u5185\u5bb9')),
                ('creater', models.CharField(max_length=255, null=True, verbose_name='\u521b\u5efa\u4eba')),
                ('createTime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('ModifyUser', models.CharField(max_length=255, null=True, verbose_name='\u4fee\u6539\u4eba')),
                ('ModifyTime', models.DateTimeField(auto_now=True, null=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
            options={
                'db_table': 'script',
                'permissions': (('view_script', '\u67e5\u770b\u811a\u672c'), ('edit_script', '\u7f16\u8f91\u811a\u672c')),
            },
        ),
    ]
