# Generated by Django 4.2.2 on 2023-09-21 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='images',
            field=models.CharField(max_length=500, verbose_name='images'),
        ),
    ]