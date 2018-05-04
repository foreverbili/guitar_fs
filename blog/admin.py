from django.contrib import admin
from . import models

# Register your models here.




class BlgAdmin(admin.ModelAdmin):
    list_display = ['name','uper','published_date']

class ComblogAdmin(admin.ModelAdmin):
    list_display = ['toblg','author','content']




admin.site.register(models.Blog,BlgAdmin)
admin.site.register(models.Comblg,ComblogAdmin)