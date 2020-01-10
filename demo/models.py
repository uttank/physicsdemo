from django.db import models

# Create your models here.

class Disk(models.Model):
    disk_number = models.CharField(max_length=2)
    title = models.CharField(max_length=100)


class Demo(models.Model):
    disk = models.ForeignKey(Disk, default="", on_delete=models.CASCADE)
    demo_number = models.CharField(max_length=2)
    title = models.CharField(max_length=50)
    movie = models.CharField(max_length=50)
    sub_chapter = models.CharField(max_length=2)
    hit_count =models.CharField(max_length=10)
    download_count = models.CharField(max_length=10)

    class Meta:
        ordering = ('demo_number',)