from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Notice)

"""
可以对字段进行过滤，不需要显示的可以不显示
"""
# class ManageMedia(admin.ModelAdmin):
#     fields = ('image',)
# admin.site.register(models.Banner, ManageMedia)
admin.site.register(models.Banner)