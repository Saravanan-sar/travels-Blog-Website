# Generated by Django 5.1.7 on 2025-03-15 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_is_published_alter_post_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img_url',
            field=models.ImageField(max_length=500, null=True, upload_to='posts/images'),
        ),
    ]
