# Generated by Django 3.0.2 on 2020-01-10 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20200110_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disk',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
