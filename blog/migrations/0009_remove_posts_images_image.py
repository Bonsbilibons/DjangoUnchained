# Generated by Django 4.2.2 on 2023-09-25 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_posts_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts_images',
            name='image',
        ),
    ]
