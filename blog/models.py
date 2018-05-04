from django.db import models
from django.utils import timezone
from gtpxz.models import Profile
# Create your models here.

#part C


class Blog(models.Model):
    name = models.CharField(max_length=32)
    uper = models.ForeignKey(Profile, related_name="pubblg", on_delete=models.CASCADE, null=True,blank=True)
    published_date = models.DateTimeField(blank=True, null=True,default=timezone.now)
    choice = {('first',u'水一贴'),
            ('second',u'技术贴'),
              ('third', u'交♂易贴'),
              ('third', u'公告贴'),
    }
    type = models.CharField(max_length=50, blank=True,choices=choice)

    def __str__(self):
        return self.name


class Comblg(models.Model):
    author = models.ForeignKey(Profile, related_name="blgcom",on_delete=models.CASCADE,null=True,blank=True)
    toblg = models.ForeignKey(Blog, related_name="reblg", on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length=500)
    CreateDate = models.DateTimeField(blank=True, null=True,default=timezone.now)

    def __str__(self):
        return self.author.nickname