# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 16:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bugs', '0002_auto_20161114_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
            },
        ),
        migrations.RemoveField(
            model_name='bug',
            name='submitter',
        ),
        migrations.AddField(
            model_name='bug',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bug_created_by_set', to=settings.AUTH_USER_MODEL, verbose_name='created by'),
        ),
        migrations.AddField(
            model_name='bug',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bug_updated_by_set', to=settings.AUTH_USER_MODEL, verbose_name='updated by'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='browser_name_other',
            field=models.CharField(blank=True, help_text='Enter the browser name only if it is not in the list of browser names.', max_length=255, verbose_name='browser name other'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='operating_system_other',
            field=models.CharField(blank=True, help_text='Enter the name of your operating system only if it is not in the list of operating systems.', max_length=255, verbose_name='operating system other'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='priority',
            field=models.IntegerField(choices=[(10, 'Low'), (20, 'Medium'), (30, 'High'), (40, 'Immediate')], help_text='The importance and urgency of resolving the error.', verbose_name='priority'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='screenshot',
            field=models.ImageField(blank=True, help_text='Upload a helpful screenshot if you have one', upload_to='bugs', verbose_name='screenshot'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='seen',
            field=models.DateTimeField(help_text='When was the bug seen?', verbose_name='date seen'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='severity',
            field=models.IntegerField(choices=[(10, 'Trivial'), (20, 'Minor'), (30, 'Major'), (40, 'Critical'), (50, 'Blocker')], help_text='The degree of the error impact on the operation of the system.', verbose_name='severity'),
        ),
        migrations.AddField(
            model_name='bug',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bugs.Project', verbose_name='project'),
        ),
    ]
