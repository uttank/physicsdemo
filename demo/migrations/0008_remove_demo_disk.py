# Generated by Django 3.0.2 on 2020-01-10 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_auto_20200110_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demo',
            name='disk',
        ),
    ]
