from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.car_photo.url))
    
    
    list_display=('id','thumbnail','car_title','color','city','model','year','body_style','fuel_type','is_featured')
    list_display_links=('id','thumbnail','car_title')
    list_editable=('is_featured',)
    search_fields=('id','car_title','color','city','model','year',)
    list_filter=('city','model','fuel_type','body_style')
admin.site.register(Car,CarAdmin)