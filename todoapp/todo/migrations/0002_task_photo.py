# Generated by Django 4.2.4 on 2023-09-01 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='todo_photos/'),
        ),
    ]
