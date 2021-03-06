# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-12 19:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Lwd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_content', models.TextField()),
                ('com_created_time', models.DateTimeField(auto_now_add=True)),
                ('com_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lwd.ArticleInfo')),
                ('com_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lwd.UserInfo')),
            ],
            options={
                'db_table': 'comment_info',
            },
        ),
    ]
