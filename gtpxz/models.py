from django.db import models
from django.utils import timezone
import time
# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=32)
    male = {('man',u'男'),
            ('woman',u'女'),
    }
    gender = models.CharField(max_length=50, blank=True,choices=male)
    age = models.IntegerField(default='20')
    memo = models.TextField()
    def __str__(self):
        return self.name
class Gtps(models.Model):
    name = models.CharField(max_length=32)
    uper = models.ForeignKey('Users',on_delete=models.CASCADE)
    #CreateDate = models.DateTimeField(default='2012-1-2 12:00')
