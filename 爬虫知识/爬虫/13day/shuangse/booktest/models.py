from django.db import models

# Create your models here.


class ShuangSeQiu(models.Model):
    hong = models.CharField(max_length=50)
    lan = models.CharField(max_length=50)
    times = models.CharField(max_length=50)



