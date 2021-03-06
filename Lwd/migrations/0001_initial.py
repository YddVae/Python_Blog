# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-12 19:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdBannerImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_img_name', models.CharField(max_length=255)),
                ('b_info_content', models.CharField(max_length=255)),
                ('b_create_time', models.DateTimeField(auto_now_add=True)),
                ('ab_img_upload', models.ImageField(max_length=255, upload_to='banner/ad_banner/%Y/%m')),
                ('ab_kind', models.CharField(default='vip_ad', max_length=255)),
                ('ab_link', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'ad_banner',
            },
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'article_category',
            },
        ),
        migrations.CreateModel(
            name='ArticleInfo',
            fields=[
                ('a_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('a_title', models.CharField(max_length=255)),
                ('a_author', models.CharField(max_length=200)),
                ('a_content_md', models.TextField()),
                ('a_content_text', models.TextField()),
                ('a_pre_img', models.CharField(default='blog_default_img.png', max_length=200)),
                ('a_word_num', models.CharField(default='0', max_length=200)),
                ('a_create_time', models.DateTimeField(auto_now_add=True)),
                ('a_update_time', models.DateTimeField(auto_now=True)),
                ('a_like_num', models.IntegerField(default=0)),
                ('a_collect_num', models.IntegerField(default=0)),
                ('a_comment_num', models.IntegerField(default=0)),
                ('a_is_publish', models.BooleanField()),
                ('a_views', models.PositiveIntegerField(default=0)),
                ('a_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lwd.ArticleCategory')),
            ],
            options={
                'db_table': 'article_info',
            },
        ),
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'article_tag',
            },
        ),
        migrations.CreateModel(
            name='CollectInfo',
            fields=[
                ('col_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('col_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lwd.ArticleInfo')),
            ],
            options={
                'db_table': 'collect_info',
            },
        ),
        migrations.CreateModel(
            name='FollowInfo',
            fields=[
                ('f_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('f_user2_name', models.CharField(default='', max_length=255)),
            ],
            options={
                'db_table': 'follow_info',
            },
        ),
        migrations.CreateModel(
            name='IndexBannerImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_img_name', models.CharField(max_length=255)),
                ('b_info_content', models.CharField(max_length=255)),
                ('b_create_time', models.DateTimeField(auto_now_add=True)),
                ('ib_img_upload', models.ImageField(max_length=255, upload_to='banner/index_banner/%Y/%m')),
                ('ib_kind', models.CharField(default='index', max_length=255)),
            ],
            options={
                'db_table': 'index_banner',
            },
        ),
        migrations.CreateModel(
            name='LikeInfo',
            fields=[
                ('l_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('l_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lwd.ArticleInfo')),
            ],
            options={
                'db_table': 'like_info',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('u_id', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('u_account', models.CharField(max_length=255, unique=True)),
                ('u_name', models.CharField(max_length=200, unique=True)),
                ('u_password', models.CharField(max_length=200)),
                ('u_img', models.CharField(default='user_default_img.png', max_length=255)),
                ('u_sex', models.CharField(default=2, max_length=20)),
                ('u_email', models.CharField(max_length=200)),
                ('u_website', models.CharField(max_length=200)),
                ('u_is_simple', models.BooleanField(default=1)),
                ('u_intro', models.TextField(default='这个人很懒，什么都没写')),
                ('u_is_delete', models.BooleanField(default=0)),
                ('u_point', models.CharField(default=0, max_length=200)),
                ('u_level', models.CharField(default=1, max_length=50)),
                ('u_lb', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('u_token', models.CharField(max_length=200)),
                ('u_follow', models.TextField(default='', null=True)),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
        migrations.AddField(
            model_name='likeinfo',
            name='l_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lwd.UserInfo'),
        ),
        migrations.AddField(
            model_name='followinfo',
            name='f_user1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lwd.UserInfo'),
        ),
        migrations.AddField(
            model_name='collectinfo',
            name='col_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lwd.UserInfo'),
        ),
        migrations.AddField(
            model_name='articleinfo',
            name='a_tag',
            field=models.ManyToManyField(blank=True, to='Lwd.ArticleTag'),
        ),
        migrations.AddField(
            model_name='articleinfo',
            name='a_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lwd.UserInfo'),
        ),
    ]
