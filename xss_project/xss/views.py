from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    name=None
    if request.method=='POST':
        name=request.POST.get('name')
    return render(request, 'home.html',{'name': name })