from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name='书名')
    publisher = models.ForeignKey('Publisher')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '书'
        verbose_name_plural = verbose_name


