from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    GENDER_TYPE = (
        ('U', '未知'),
        ('M', '男'),
        ('F','女'),
    )
    user = models.ForeignKey(User, unique=True)
    real_name = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=GENDER_TYPE)
    company = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    occupation = models.CharField(max_length=100)
    level = models.IntegerField()
    upload_num = models.IntegerField()
    balance = models.IntegerField()
    reg_date = models.DateTimeField()
