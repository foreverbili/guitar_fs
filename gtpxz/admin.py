from django.contrib import admin
from . import models

from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.models import Group as DjangoGroup
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# Register your models here.

class GtpAdmin(admin.ModelAdmin):
    list_display = ['name','uper','published_date','type']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content','author']

class TypeAdmin(admin.ModelAdmin):
    list_display = ['type']

class UserAdmin(UserAdmin):
    list_display = ['nickname', 'gender', 'age', 'intro', 'id']




admin.site.register(models.User,UserAdmin)
admin.site.register(models.Gtp,GtpAdmin)
admin.site.register(models.Comment,CommentAdmin)
admin.site.register(models.Type,TypeAdmin)