# Generated by Django 3.0.2 on 2020-01-10 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0009_demo_disk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demo',
            name='disk',
        ),
    ]
