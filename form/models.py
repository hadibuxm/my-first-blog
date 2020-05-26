from django.db import models

# Create your models here.
class Exam_form(models.Model):
    ANNUAL='A'
    SUPPLY='S'
    exam=[
        (ANNUAL,'ANNUAL'),
        (SUPPLY,'SUPPLY')
    ]
    name=models.CharField(max_length=20)
    second_name=models.CharField(max_length=20)
    father_name=models.CharField(max_length=20)
    roll_no=models.CharField(max_length=7)
    mobile_no=models.IntegerField(default=00000000000)
    sex=models.CharField(max_length=5)
    email_id=models.TextField(max_length=50)
    campus=models.TextField(max_length=100)
    annual_supply=models.CharField(max_length=7)
    fee_challan=models.IntegerField(default=0)
    department=models.TextField(max_length=100)
    sub1=models.CharField(max_length=20)
    sub2=models.CharField(max_length=20)
    sub3=models.CharField(max_length=20)
    sub4=models.CharField(max_length=20)
    sub5=models.CharField(max_length=20)