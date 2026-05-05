from django.shortcuts import render
from .models import Student

def index(request):
    return render(request, "index.html")

def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST.get("name"),
            usn=request.POST.get("usn"),
            grade=request.POST.get("grade")
        )
    return render(request, "index.html")

def grade_o(request):
    students = Student.objects.filter(grade__iexact='O')
    return render(request, "result.html", {"students": students})