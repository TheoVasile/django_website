# Generated by Django 2.2.1 on 2019-05-22 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190521_2231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='content',
            new_name='article_content',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='published',
            new_name='article_published',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='article_title',
        ),
        migrations.RenameField(
            model_name='articleseries',
            old_name='article_category',
            new_name='series_category',
        ),
    ]
