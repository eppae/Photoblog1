from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
# Create your models here.
class Customuser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission,related_name='custom_user_permissions')
    pass
class Userprofile(models.Model):
    lastName = models.CharField(max_length=40)
    firstName = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=20)
    email = models.EmailField
    state = models.CharField(max_length=40)
    Janre = models.TextField
    language = models.CharField(max_length=2,choices=[
        ('kr', 'Korea, Republic of'),
        ('en', 'English'),
        ('fr', 'French'),
        ('de', 'German'),
        ('pt', 'Portuguese'),
    ])
    gender = models.CharField(max_length=6,choices=[
        ('male','남'),
        ('female','여'),
    ])