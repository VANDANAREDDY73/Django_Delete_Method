from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.
def dept(request):
  QLDO=Dept.objects.all()
  QLDO=Dept.objects.filter(DEPT_NO=10,LOC='NEW YORK')
  d={'Depts':QLDO}
  return render(request,'dept.html',d)

def emp(request):
  QLEO=Emp.objects.all()
  QLEO=Emp.objects.filter(Q(ENAME__startswith='J')&Q(DEPT_NO=20))
  QLEO=Emp.objects.filter(Q(ENAME__startswith='J')|Q(DEPT_NO=20))
  QLEO=Emp.objects.all()
  
  d={'Emps':QLEO}
  return render(request,'emp.html',d)

def insert_dept(request):
  D=input('ENTER DEPT_NO : ')
  name=input('ENTER NAME: ')
  location=input('ENTER LOCATION: ')
  
  NDTO=Dept.objects.get_or_create(DEPT_NO=D,DNAME=name,LOC=location)[0]
  NDTO.save()
  DO=Dept.objects.all()
  d={'Depts':DO}

  return render(request,'dept.html',d)




def insert_emp(request):
  E=int(input('Enter Emp no: '))
  En=input('Enter Name: ')
  j=input('Enter job name: ')
  m=int(input('Enter MGR no: '))
  hr=input('Enter date: ')
  s=int(input('Enter salary: '))
  comm=int(input('Enter comm: '))
  D=input('enter dept_no: ')

  DO=Dept.objects.get(DEPT_NO=D)
  NEO=Emp.objects.get_or_create(EMPNO=E,ENAME=En,JOB=j,MGR=m,HIREDATE=hr,SAL=s, COMM=comm,DEPT_NO=DO)[0]
  NEO.save()

  EO=Emp.objects.all()
  d={'Emps':EO}
  return render(request,'emp.html',d)


def insert_salgrade(request):
  pk=input('Enter pk value: ')
  g=int(input('enter grade: '))
  l=int(input('enter lowsal: '))
  h=int(input('Enter highsal: '))
  NSO=Salgrade.objects.get_or_create(pk=pk,GRADE=g,LOSAL=l,HISAL=h)[0]
  NSO.save()

  SO=Salgrade.objects.all()
  d={'Sals':SO}
  return render(request,'salgrade.html',d)
  

def update_emp(request):

  #Emp.objects.filter(JOB='CLERK').update(ENAME='JACK')
  DO=Dept.objects.get(DEPT_NO=4)
  DO.save()
  EO=Emp.objects.get_or_create(DEPT_NO=DO)
  EO.save()
  Emp.objects.update_or_create(JOB='ENGINEER',defaults={'DEPT_NO':EO})
  EO=Emp.objects.all()
  d={'Emps':EO}
  return render(request,'emp.html',d)


def delete_salgrade(request):

  Salgrade.objects.all().delete()
  SO=Salgrade.objects.all()
  d={'Sals':SO}
  return render(request,'salgrade.html',d)

def delete_emp(request):

  Emp.objects.filter(ENAME='BHARGAVI').delete()
  EO=Emp.objects.all()
  d={'Emps':EO}
  return render(request,'emp.html',d)







