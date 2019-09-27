from django.db import models


# Create your models here.

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()

    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    bname = models.CharField(max_length=20)
    bgender = models.BooleanField()
    bcontent = models.CharField(max_length=200)
    hbook = models.ForeignKey(BookInfo)

    def __str__(self):
        return self.bname
