from django.db import models
from django.utils import timezone
from gtpxz.models import Profile
# Create your models here.

#part C


class Video(models.Model):
    name = models.CharField(max_length=32)
    uper = models.ForeignKey(Profile,related_name="pubvid",on_delete=models.CASCADE,null=True,blank=True)
    published_date = models.DateTimeField(blank=True, null=True,default=timezone.now)

    def __str__(self):
        return self.name


class Comvid(models.Model):
    author = models.ForeignKey(Profile, related_name="vidcom",on_delete=models.CASCADE,null=True,blank=True)
    tovid = models.ForeignKey(Video, related_name="revid", on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length=500)
    CreateDate = models.DateTimeField(blank=True, null=True,default=timezone.now)

    def __str__(self):
        return self.author.nickname