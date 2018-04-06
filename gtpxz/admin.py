from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models

# Register your models here.

class UsersInline(admin.StackedInline):
    model = models.Users
    max_num = 1
    can_delete = False

class UsersAdmin(BaseUserAdmin):
    inlines = (UsersInline,)

class GtpsAdmin(admin.ModelAdmin):
    list_display = ['name','uper','published_date']

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['content','author']


admin.site.unregister(User)
admin.site.register(User,UsersAdmin)
admin.site.register(models.Gtps,GtpsAdmin)
admin.site.register(models.Comments,CommentsAdmin)