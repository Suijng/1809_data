from django.db import models
from datetime import datetime
# Create your models here.

class Nav(models.Manager):
    name=models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    create_time=models.DateTimeField(auto_now_add=True )


