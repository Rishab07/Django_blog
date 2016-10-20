# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-16 12:56
from __future__ import unicode_literals

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=56)),
                ('content', models.CharField(max_length=167)),
                ('feeling', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_location)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]