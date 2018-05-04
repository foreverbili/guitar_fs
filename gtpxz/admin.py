from django.contrib import admin
from . import models


# Register your models here.





class CommentAdmin(admin.ModelAdmin):
    list_display = ['togtp','author','content']


class GtpAdmin(admin.ModelAdmin):
    list_display = ['name','uper','published_date']















admin.site.register(models.Profile)
admin.site.register(models.Comgtp,CommentAdmin)

admin.site.register(models.Gtp,GtpAdmin)



