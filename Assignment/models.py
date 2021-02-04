from django.db import models

# Create your models here.
class Users(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.username
