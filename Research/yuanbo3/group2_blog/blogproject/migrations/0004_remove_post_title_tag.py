# Generated by Django 4.1.7 on 2023-03-03 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogproject', '0003_alter_post_title_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title_tag',
        ),
    ]
