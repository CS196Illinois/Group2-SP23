# Generated by Django 4.1.7 on 2023-03-03 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogproject', '0002_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='my awesome blog', max_length=255),
        ),
    ]
