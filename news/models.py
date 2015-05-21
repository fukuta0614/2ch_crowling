from django.db import models
import datetime

# Create your models here.
class News(models.Model):
    base_site = models.CharField(max_length=120,default='unknown')
    title = models.CharField(max_length=120,default='notitle')
    link = models.CharField(max_length=120,default='nolink')
    # description = models.TextField(blank=True,null=True)
    # creator = models.CharField(max_length=120,blank=True)
    date = models.DateTimeField(default=datetime.datetime.now)
    subject = models.CharField(max_length=120,blank=True,null=True)
    # encoded = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title
    # for_you = models.BooleanField(default=True,verbose_name='Check this')
    # updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    class Meta:
        ordering = ('-date',)

class User(models.Model):
    user_name = models.CharField(max_length=120,null=True,blank=True)
