from django.db import models

# Create your models here.
class Userinfo(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    createCounttime = models.DateTimeField(auto_now_add=True)

class Yfc_userid(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Studentinfor(models.Model):
    stuid = models.ForeignKey('Userinfo', to_field='userid', on_delete='CASCADE')
    name = models.CharField(max_length=20)
    age = models.IntegerField(max_length=3)
    gendle = models.BooleanField()
    classes = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    result = models.FloatField()
