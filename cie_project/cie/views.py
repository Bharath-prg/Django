from django.shortcuts import render
from .models import Marks
# Create your views here.
def home(request):
    if request.method=='POST' :
        Marks.objects.create(
        usn=request.POST.get('usn'),
        name=request.POST.get('name'),
        sub_code=request.POST.get('sub_code'),
        cie=request.POST.get('cie'),
        )
    return render(request,'home.html')

def lowcie(request):
    students=Marks.objects.filter(cie__lt=20)
    return render(request,'lowcie.html',{'students':students})