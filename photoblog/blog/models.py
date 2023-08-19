from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    name = models.CharField(max_length=30)
    birth = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    author =models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=40)
    content = models.TextField()

    def __str__(self):
        return self.title