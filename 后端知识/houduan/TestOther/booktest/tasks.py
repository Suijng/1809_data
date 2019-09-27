from django.test import TestCase
import time
from celery import task


# Create your tests here.
@task
def say():
    print('1')
    time.sleep(3)
    print('2')
