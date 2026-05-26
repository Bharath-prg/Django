from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField()
    usn=models.CharField()
    sem=models.IntegerField()
    fee=models.BooleanField()

    class Meta:
        unique_together=('usn','sem')