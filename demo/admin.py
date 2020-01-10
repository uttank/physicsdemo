from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

from demo.models import Disk, Demo


class DemoResources(resources.ModelResource):
    
    class Meta:
        model = Demo

class DemoAdmin(ImportExportModelAdmin):
    resource_class = DemoResources

admin.site.register(Disk)
admin.site.register(Demo, DemoAdmin)