# Generated by Django 4.2.2 on 2023-09-16 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_user_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=None, verbose_name='updated_at'),
            preserve_default=False,
        ),
    ]