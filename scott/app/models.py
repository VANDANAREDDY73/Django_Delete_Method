from django.db import models

# Create your models here.
class Dept(models.Model):
  DEPT_NO = models.IntegerField(primary_key=True)
  DNAME = models.CharField(max_length=100)
  LOC = models.CharField(max_length=100)
  def __str__(self):
    return self.DNAME  

class Emp(models.Model):
  EMPNO = models.IntegerField()
  ENAME = models.CharField(max_length=100)
  JOB   = models.CharField(max_length=100)
  MGR   = models.IntegerField()
  HIREDATE = models.DateField()
  SAL   = models.IntegerField()
  COMM  = models.IntegerField()
  DEPT_NO = models.ForeignKey(Dept,on_delete=models.CASCADE)
  def __str__(self):
    return self.ENAME
class Salgrade(models.Model):
  GRADE = models.IntegerField()
  LOSAL = models.IntegerField()
  HISAL = models.IntegerField()

class Bonus(models.Model):
  Increment = models.IntegerField()