from django.db import models

# Create your models here.
class Country(models.Model):
  Cname=models.CharField(max_length=100,primary_key=True)
  code=models.CharField(max_length=100)