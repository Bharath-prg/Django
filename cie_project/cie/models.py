from django.db import models

# Create your models here.
class Marks(models.Model):
    usn=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    sub_code=models.CharField(max_length=10)
    cie=models.IntegerField()
    class Meta:
        unique_together=('usn','sub_code')