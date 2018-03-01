from django.contrib import admin
from .models import Users
from .models import Gtps


# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ['name','gender','age','memo','id']
admin.site.register(Users,UsersAdmin)
class GtpsAdmin(admin.ModelAdmin):
    list_display = ['name','uper','id']
admin.site.register(Gtps,GtpsAdmin)