# Generated by Django 4.1.7 on 2023-04-02 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogproject', '0013_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=255),
        ),
    ]
