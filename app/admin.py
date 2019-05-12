from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Item
from import_export.admin import ImportExportModelAdmin

class ItemAdmin(ImportExportModelAdmin):
    list_display = ('id','name','category','info','image','cost')
    list_display_links = ('id','name')
    list_editable = ('info',)
    list_per_page = 10
    search_fields = ('name','category','info')
    list_filter = ('category','date_added')


admin.site.register(Item,ItemAdmin)
admin.site.unregister(Group)