from django.shortcuts import render
from django.db import IntegrityError
from .models import Student

# Create your views here.
def index(request):
    students=Student.objects.all()
    return render(request,'index.html',{'students':students})

def add_student(request):
    error=None
    if request.method=='POST':
        try:
            Student.objects.create(
                name=request.POST.get('name'),
                usn=request.POST.get('usn'),
                sem=request.POST.get('sem'),
                fee=request.POST.get('fee')
            )
        except IntegrityError:
            error={'msg':"This entry already exists"}
        students=Student.objects.all()
        return render(request,'index.html',{'students':students,'error':error})
    
def delete_student(request):
    Student.objects.filter(fee=False).delete()
    students=Student.objects.all()
    return render(request,'index.html',{'students':students})