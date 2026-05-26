from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def display(request):
    if request.method=='POST':
        details={
            'name' : request.POST.get('name'),
            'age' : request.POST.get('age'),
            'email' : request.POST.get('email'),
            'phone' : request.POST.get('phone'),
            'address' : request.POST.get('address'),
        }

        return render(request,'display.html',{'details' : details})