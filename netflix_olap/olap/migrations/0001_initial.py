# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('watched_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PopularGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('genre_id', models.IntegerField()),
                ('genre_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PopularMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('movie_id', models.IntegerField()),
                ('movie_name', models.CharField(max_length=255)),
                ('ratings_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PopularPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('plan_id', models.IntegerField()),
                ('plan_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PopularShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('show_id', models.IntegerField()),
                ('show_name', models.CharField(max_length=255)),
                ('ratings_id', models.IntegerField()),
            ],
        ),
    ]
