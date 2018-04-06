from __future__ import unicode_literals
from firstpro import settings

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone

# Create your models here.
class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    male = {('man',u'男'),
            ('woman',u'女'),
    }
    gender = models.CharField(max_length=50, blank=True,choices=male)
    age = models.IntegerField(default='20')
    memo = models.TextField()


    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

    class Meta:
        db_table = 'Users'


    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                p = Users.objects.get(user=self.user)
                self.pk = p.pk
            except Users.DoesNotExist:
                pass

        super(Users, self).save(*args, **kwargs)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Users()
        profile.user = instance
        profile.save()

post_save.connect(create_user_profile, sender=User)


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
    author = models.ForeignKey('Users', on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    CreateDate = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return 'comments'