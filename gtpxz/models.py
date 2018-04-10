from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone



# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=30, blank=True)
    male = {('man',u'男'),
            ('woman',u'女'),
    }
    gender = models.CharField(max_length=50, blank=True,choices=male)
    age = models.IntegerField(default='20')
    intro = models.TextField(blank=True)

    def __str__(self):
        return self.nickname

    class Meta(AbstractUser.Meta):
        pass

class Type(models.Model):
    type=models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.type

class Gtp(models.Model):
    name = models.CharField(max_length=32)
    uper = models.ForeignKey(to=User,related_name="public",on_delete=models.CASCADE,null=True,blank=True)
    published_date = models.DateTimeField(blank=True ,null=True)
    type=models.ForeignKey(to=Type,related_name="type_belong",null=True,blank=True,default=None)

    def publish(self):
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        return self.name

class Comment(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE,null=True,blank=True)
    content = models.CharField(max_length=500)
    CreateDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'comments'