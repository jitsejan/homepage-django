# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160728_2359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', django_markdown.models.MarkdownField()),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('image', models.CharField(max_length=300)),
                ('link', models.CharField(max_length=200)),
                ('publish', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Website Entry',
                'verbose_name_plural': 'Website Entries',
            },
            bases=(models.Model,),
        ),
    ]
