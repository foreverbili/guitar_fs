from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=30, blank=True)
    male = {('man',u'男'),
            ('woman',u'女'),
    }
    gender = models.CharField(max_length=50, blank=True,choices=male)
    age = models.IntegerField(default='20')
    intro = models.TextField(blank=True)

    def __str__(self):
        return '{}({})' .format(self.nickname,self.user)


#part A


class Gtp(models.Model):
    name = models.CharField(max_length=32)
    gtp = models.FileField(upload_to='gtp/gtps/%Y/%m/%d/',blank=True, null=True)
    cover = models.ImageField(upload_to='gtp/covers/%Y/%m/%d/',blank=True, null=True)
    uper = models.ForeignKey(Profile,related_name="pubgtp",on_delete=models.CASCADE,null=True,blank=True)
    published_date = models.DateTimeField(blank=True, null=True,default=timezone.now)


    def __str__(self):
        return self.name




# part public
class Comgtp(models.Model):
    author = models.ForeignKey(Profile, related_name="gtpcom",on_delete=models.CASCADE,null=True,blank=True)
    togtp = models.ForeignKey(Gtp,related_name="regtp", on_delete=models.CASCADE,null=True,blank=True)
    content = models.CharField(max_length=500)
    CreateDate = models.DateTimeField(blank=True, null=True,default=timezone.now)

    def __str__(self):
        return self.author.nickname

