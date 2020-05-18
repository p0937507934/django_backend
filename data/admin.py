from django.contrib import admin
from .models import Data
from import_export.admin import ExportActionModelAdmin
# Register your models here.



@admin.register(Data)
class ExportDataAdmin(ExportActionModelAdmin):
    # readonly_fields=['Measurement_Date']
    list_display=['Measurement_Date','config_id','user_id','device_id']
    

admin.site.site_title='後台管理系統'
admin.site.site_header='後台管理系統'
admin.site.index_title='歡迎登入'
# admin.site.register(Data,DataAdmin)s