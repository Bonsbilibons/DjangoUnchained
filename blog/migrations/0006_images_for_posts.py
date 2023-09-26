# Generated by Django 4.2.2 on 2023-09-25 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_posts_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images_for_posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='title')),
                ('image', models.CharField(max_length=100, verbose_name='image')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.posts')),
            ],
            options={
                'db_table': 'images_for_posts',
            },
        ),
    ]
