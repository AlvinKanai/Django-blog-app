# Generated by Django 4.0 on 2022-01-07 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_remove_post_view_count_postview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment_count',
        ),
    ]
