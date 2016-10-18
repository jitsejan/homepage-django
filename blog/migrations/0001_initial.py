# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-17 15:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_markdown.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        # migrations.CreateModel(
        #     name='Entry',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('title', models.CharField(max_length=200)),
        #         ('body', django_markdown.models.MarkdownField()),
        #         ('slug', models.SlugField(max_length=200, unique=True)),
        #         ('publish', models.BooleanField(default=False)),
        #         ('created', models.DateTimeField(auto_now_add=True)),
        #         ('modified', models.DateTimeField(auto_now=True)),
        #     ],
        #     options={
        #         'ordering': ['-created'],
        #         'verbose_name': 'Blog Entry',
        #         'verbose_name_plural': 'Blog Entries',
        #     },
        # ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flickr_id', models.CharField(default=b'No id', max_length=50)),
                ('title', models.CharField(default=b'No title', max_length=200)),
                ('description', models.CharField(default=b'No description', max_length=300)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('date_taken', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(max_length=300)),
                ('image_url', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
            },
        ),
        migrations.CreateModel(
            name='Photoset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flickr_id', models.CharField(default=b'No id', max_length=50)),
                ('secret', models.CharField(default=b'No secret', max_length=50)),
                ('title', models.CharField(default=b'No title', max_length=200)),
                ('description', models.CharField(default=b'No description', max_length=300)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Photoset',
                'verbose_name_plural': 'Photosets',
            },
        ),
        # migrations.CreateModel(
        #     name='Project',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('title', models.CharField(max_length=200)),
        #         ('description', django_markdown.models.MarkdownField()),
        #         ('slug', models.SlugField(max_length=200, unique=True)),
        #         ('image', models.CharField(max_length=300)),
        #         ('link', models.CharField(max_length=200)),
        #         ('publish', models.BooleanField(default=False)),
        #         ('created', models.DateTimeField(auto_now_add=True)),
        #         ('modified', models.DateTimeField(auto_now=True)),
        #     ],
        #     options={
        #         'ordering': ['-created'],
        #         'verbose_name': 'Project Entry',
        #         'verbose_name_plural': 'Project Entries',
        #     },
        # ),
        # migrations.CreateModel(
        #     name='Tag',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('slug', models.SlugField(max_length=200, unique=True)),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='Website',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('title', models.CharField(max_length=200)),
        #         ('description', django_markdown.models.MarkdownField()),
        #         ('slug', models.SlugField(max_length=200, unique=True)),
        #         ('image', models.CharField(max_length=300)),
        #         ('link', models.CharField(max_length=200)),
        #         ('publish', models.BooleanField(default=False)),
        #         ('created', models.DateTimeField(auto_now_add=True)),
        #         ('modified', models.DateTimeField(auto_now=True)),
        #     ],
        #     options={
        #         'ordering': ['-created'],
        #         'verbose_name': 'Website Entry',
        #         'verbose_name_plural': 'Website Entries',
        #     },
        # ),
        migrations.AddField(
            model_name='photo',
            name='photoset',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='blog.Photoset'),
        ),
        # migrations.AddField(
        #     model_name='entry',
        #     name='tags',
        #     field=models.ManyToManyField(to='blog.Tag'),
        # ),
    ]

