from django.db import models
from django.contrib.auth.models import User

class prodacts(models.Model):
    p_name=models.CharField(max_length=70,null=False,blank=False)
    color=models.CharField(max_length=70,null=True,blank=True)
    price=models.IntegerField(null=False,blank=False)

    def __str__(self):
        return self.p_name
