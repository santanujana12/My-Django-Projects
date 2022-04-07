from pyexpat import model
from django.db import models

# Create your models here.
class Library(models.Model):
    id = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=30)
    bauthor = models.CharField(max_length=30)
    issued = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.bname
