# Generated by Django 4.2.2 on 2023-09-25 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_images_for_posts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images_for_posts',
            new_name='Posts_Images',
        ),
        migrations.AlterModelTable(
            name='posts_images',
            table='Posts_Images',
        ),
    ]