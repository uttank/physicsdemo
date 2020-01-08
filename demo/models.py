from django.db import models

# Create your models here.

class Demo_number(models.Model):
    disk_number = models.CharField(max_length=2)


class Demo(models.Model):
    disk_number = models.ForeignKey(Demo_number, on_delete=models.CASCADE)
    demo_number = models.CharField(max_length=2)
    title = models.CharField(max_length=50)
    movie = models.CharField(max_length=50)
    sub_chapter = models.CharField(max_length=2)
    hit_count =models.CharField(max_length=10)
    download_count = models.CharField(max_length=10)

    class Meta:
        ordering = ('demo_number',)