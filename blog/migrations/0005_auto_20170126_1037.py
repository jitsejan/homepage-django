# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-26 10:37
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_entry_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('imagefile', models.ImageField(upload_to=b'images')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='entry',
            name='description',
            field=django_markdown.models.MarkdownField(blank=True, default=b''),
        ),
    ]