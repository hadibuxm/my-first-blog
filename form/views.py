from django.shortcuts import render
from .models import Exam_form
from django.http import HttpResponseRedirect
# Create your views here.
def Exam_View(request):
    exam=Exam_form.objects.all()
    return render(request,'form.html',{'exam':exam})
#############################################33
def addform(request):
    _submit=Exam_form(name=request.POST['name'],second_name=request.POST['secondname'],
                      father_name=request.POST['fathername'],roll_no=request.POST['rollno'],
                      mobile_no=request.POST['mobile'],sex=request.POST['gender'],
                      email_id=request.POST['emailid'],campus=request.POST['campus'],
                      annual_supply=request.POST['annualsupply'],fee_challan=request.POST['challanno'],
                      department=request.POST['department'],sub1=request.POST['subject1'],
                      sub3=request.POST['subject2'],
                      sub4=request.POST['subject4'],sub5=request.POST['subject5'],)
    _submit.save()
    #_secondname=Exam_form(second_name=request.POST['secondname'])
    #_secondname=Exam_Form(second_name=request.Post['secondname'])
    #_secondname.save()
    return HttpResponseRedirect('/form/')