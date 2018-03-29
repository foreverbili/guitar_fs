from django.db import models
from django.utils import timezone

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
    published_date = models.DateTimeField(blank=True ,null=True)
    def publish(self):
        self.published_date = timezone.now
        self.save()
    def __str__(self):
        return self.name

class Comments(models.Model):
    content = models.CharField(max_length=500)
    author = models.ForeignKey('Users',on_delete=models.CASCADE)
    CreateDate = models.DateTimeField(default=timezone.now)