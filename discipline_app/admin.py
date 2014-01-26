from django.contrib import admin
from discipline_app.models import *

class CategoryAdmin(admin.ModelAdmin):
  fields = ('name',)
admin.site.register(Category, CategoryAdmin)

class BlockAdmin(admin.ModelAdmin):
  fields = ('person', 'start_time', 'end_time', 'category')
admin.site.register(Block, BlockAdmin)

class SiteAdmin(admin.ModelAdmin):
  fields = ('url', 'hostname')
admin.site.register(Site, SiteAdmin)
