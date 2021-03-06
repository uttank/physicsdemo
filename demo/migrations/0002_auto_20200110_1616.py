# Generated by Django 3.0.2 on 2020-01-10 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disk_number', models.CharField(max_length=2)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='demo',
            name='disk_number',
        ),
        migrations.DeleteModel(
            name='Demo_number',
        ),
        migrations.AddField(
            model_name='demo',
            name='disk',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='demo.Disk'),
        ),
    ]
