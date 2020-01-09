from django.contrib import admin

# Register your models here.
from demo.models import Disk, Demo

admin.site.register(Disk)
admin.site.register(Demo)