from django.shortcuts import render
from .models import Student

def index(request):
    return render(request, "index.html")

def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST.get("name"),
            usn=request.POST.get("usn"),
            dept=request.POST.get("dept"),
            grade=request.POST.get("grade")
        )
    return render(request, "index.html")

def update_grade(request):
    students = []
    if request.method == "POST":
        name = request.POST.get("name")
        grade = request.POST.get("grade")
        Student.objects.filter(name=name).update(grade=grade)
        students = Student.objects.filter(name=name)
    return render(request, "result.html", {"students": students})

def view_students(request):
    students = Student.objects.all()
    return render(request, "result.html", {"students": students})