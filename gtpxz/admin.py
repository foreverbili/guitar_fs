from django.contrib import admin
from . import models

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['nickname','gender','age','intro','id']

class GtpAdmin(admin.ModelAdmin):
    list_display = ['name','uper','published_date','type']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content','author']

class TypeAdmin(admin.ModelAdmin):
    list_display = ['type']



admin.site.register(models.User,UserAdmin)
admin.site.register(models.Gtp,GtpAdmin)
admin.site.register(models.Comment,CommentAdmin)
admin.site.register(models.Type,TypeAdmin)