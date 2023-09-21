# Generated by Django 4.2.2 on 2023-09-21 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_user_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.CharField(max_length=2000, verbose_name='description')),
                ('images', models.CharField(max_length=50, verbose_name='images')),
                ('updated_at', models.DateTimeField(verbose_name='updated_at')),
                ('created_at', models.DateTimeField(verbose_name='created_at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'posts',
            },
        ),
    ]