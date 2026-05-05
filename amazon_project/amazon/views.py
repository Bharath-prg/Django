from django.shortcuts import render
from .models import Student

def index(request):
    return render(request, "index.html")

def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            usn=request.POST.get("usn"),
            name=request.POST.get("name"),
            company=request.POST.get("company")
        )
    return render(request, "index.html")

def amazon_students(request):
    students = Student.objects.filter(company__iexact="Amazon")
    return render(request, "result.html", {"students": students})