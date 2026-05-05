from django.shortcuts import render
from .models import Employee

def index(request):
    return render(request, "index.html")

def add_employee(request):
    if request.method == "POST":
        Employee.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            date=request.POST.get("date"),
            job=request.POST.get("job"),
            salary=request.POST.get("salary")
        )
    return render(request, "index.html")

def high_salary(request):
    emp = Employee.objects.filter(salary__gt=50000)
    return render(request, "result.html", {"emp": emp})