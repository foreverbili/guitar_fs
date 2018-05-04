from django.contrib import admin
from . import models

# Register your models here.



class VidAdmin(admin.ModelAdmin):
    list_display = ['name','uper','published_date']

class ComvideAdmin(admin.ModelAdmin):
    list_display = ['tovid','author','content']


admin.site.register(models.Video,VidAdmin)
admin.site.register(models.Comvid,ComvideAdmin)

